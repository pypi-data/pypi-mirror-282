"""
Make a tool work as a distributed service

Pushing messages proactively

Distributed tool must know the endpoint of the scheduler.

Each registered tool has a ToolProxy class to store websocket connection 
"""

import json
import os
import queue
import threading
import uuid
from contextlib import contextmanager
from typing import Dict, Generator, Generic, List, Optional, Tuple, Union

from flask import Flask, request
from flask_sock import ConnectionClosed as WSConnectionClosed
from flask_sock import Server as WSServer
from flask_sock import Sock

from .log import logger
from .messages import FileUploadResponse, RestResponse, WSToolMsgParser
from .models import (
    C,
    Result,
    SchedulerCommand,
    SchedulerCommandDictType,
    SchedulerCommandResponse,
    Status,
    StatusInfo,
    Trigger,
    WSSchedulerRawMsgType,
    WSToolRawMsgType,
)


class ToolRemoteRef:
    """
    A class containing reference to remote tools
    """

    _scheduler_command_session_queues: Dict[
        str, "queue.Queue[SchedulerCommandResponse]"
    ] = {}

    def __init__(self, uuid: str, name: str, ws: WSServer) -> None:
        self.name = name
        self.ws = ws
        self.uuid = uuid
        self.status = StatusInfo("", -1, -1, Status.OFFLINE)

    def send_command(self, cmd_type: Trigger, cmd_data: Dict) -> Tuple[str, bool]:
        """
        Send command to the tool by websocket
        """
        request_uuid: str = uuid.uuid4().hex
        scheduler_cmd = SchedulerCommand.create_dict(
            request_uuid, {"type": cmd_type, "data": cmd_data}
        )
        with self.wait_command_response(scheduler_cmd, request_uuid) as msg:
            if msg is None:
                return "queue wait timeout!", False
            return msg.msg, msg.success

    @contextmanager
    def wait_command_response(
        self, scheduler_cmd: SchedulerCommandDictType, req_uuid: str
    ) -> Generator[Optional[SchedulerCommandResponse], None, None]:
        """
        A context manager to manage the temporary queue.
        """
        scheduler_msg = WSSchedulerRawMsgType(type="command", data=scheduler_cmd)
        self.ws.send(json.dumps(scheduler_msg))
        self._scheduler_command_session_queues[req_uuid] = queue.Queue(1)
        try:
            yield self._scheduler_command_session_queues[req_uuid].get(timeout=5)
        except queue.Empty:
            yield None
        finally:
            self._scheduler_command_session_queues.pop(req_uuid)

    @classmethod
    def put_response(cls, resp: SchedulerCommandResponse):
        """
        The `start_task` and `stop_task` procedure will be blocked until
        the response is put into the corresponding queue.
        """
        cls._scheduler_command_session_queues[resp.uuid].put(resp)

    def update_status_info(self, status_info: StatusInfo):
        self.status = status_info

    def __repr__(self) -> str:
        return f"<{self.__class__.__name__} {self.__dict__}>"


class RemoteTools:
    def __init__(self) -> None:
        self.tools: Dict[str, ToolRemoteRef] = {}

    def list_tools(self) -> List[ToolRemoteRef]:
        return [v for _, v in self.tools.items()]

    def add(self, tool: ToolRemoteRef):
        self.tools[tool.uuid] = tool

    def remove(self, tool: ToolRemoteRef):
        self.tools.pop(tool.uuid)

    def get_tools_by_name(self, name: str) -> List[ToolRemoteRef]:
        """
        Get tools by name
        """
        return list(filter(lambda tool: tool.name == name, self.tools.values()))

    def __repr__(self) -> str:
        return f"<{self.__class__.__name__} {self.tools}>"


class Scheduler(Generic[C]):
    def __init__(
        self,
        host: str = "0.0.0.0",
        port: int = 8681,
        root_folder=".PyBirdViewCode",
        scheduler_address: str = "",
    ) -> None:
        self.root_folder = root_folder
        if not os.path.exists(self.root_folder):
            os.makedirs(self.root_folder)

        self.files_storage_path = os.path.join(self.root_folder, "files")
        if not os.path.exists(self.files_storage_path):
            os.makedirs(self.files_storage_path)

        abs_path = lambda f: os.path.abspath(os.path.join(os.path.dirname(__file__), f))

        self.app = Flask(__name__, static_folder=abs_path("./static"))
        self.port = port
        self.host = host

        self.app.config["SOCK_SERVER_OPTIONS"] = {"ping_interval": 25}
        sock = Sock(self.app)

        self._ws_recv_msg_queue: queue.Queue[Tuple[ToolRemoteRef, WSToolRawMsgType]] = (
            queue.Queue()
        )
        sock.route("/api/websocket/<path:tool_name>/<path:uuid>")(self.handle_websocket)
        self._message_handling_thread = threading.Thread(
            target=self._task_handle_message
        )
        self._message_handling_thread.daemon = True

        # self._tasks_scheduling_thread = threading.Thread(
        #     target=self._task_schedule_tool_tasks
        # )
        # self._tasks_scheduling_thread.daemon = True

        # Task queue stores the json-serializable dictionaries as data for each task

        self._tasks: Dict[str, queue.Queue[Dict]] = {}
        self._tools = RemoteTools()
        self._results: queue.Queue[Result] = queue.Queue()

        self.app.add_url_rule(
            "/register", view_func=self.handle_register, methods=["POST"]
        )
        self.app.add_url_rule(
            "/api/tasks/get", view_func=self.handle_get_task, methods=["GET"]
        )
        self.app.add_url_rule(
            "/api/files/upload", view_func=self.handle_file_upload, methods=["POST"]
        )

    @property
    def tools_manager(self) -> RemoteTools:
        return self._tools

    def handle_websocket(self, ws: WSServer, tool_name: str, uuid: str):
        tool_ref = ToolRemoteRef(uuid, tool_name, ws)
        self._tools.add(tool_ref)
        while True:
            try:
                msg: Union[str, bytes] = ws.receive()
                try:
                    data: WSToolRawMsgType = json.loads(msg)
                    self._ws_recv_msg_queue.put((tool_ref, data))
                except json.JSONDecodeError:
                    logger.error(f"Cannot decode message: {msg}")
            except WSConnectionClosed as e:
                self._tools.remove(tool_ref)
                raise e

    def handle_file_upload(self):
        file = request.files["file"]
        if file:
            assert file.filename is not None
            ext = os.path.splitext(file.filename)[1]
            uuid_name = uuid.uuid4().hex + ext
            file.save(os.path.join(self.files_storage_path, uuid_name))
            return RestResponse("succeeded", FileUploadResponse(uuid_name)).to_dict()
        return "No file uploaded"

    def handle_get_task(self):
        """
        Handle getting task from the server
        """
        tool_name = request.args.get("tool_name")
        if tool_name is None or tool_name == "":
            return RestResponse("tool name should not be 0", None).to_dict(), 400
        try:
            return (
                RestResponse.dict_from_msg(
                    "succeeded", self._tasks[tool_name].get_nowait()
                ),
                200,
            )
        except queue.Empty:
            return (
                RestResponse(f"No task for tool {tool_name} right now").to_dict(),
                404,
            )

    def handle_register(self):
        """
        Handle tool registration
        """
        return ""

    def _task_handle_message(self):
        """
        Handle websocket messages
        """
        while 1:
            msg: WSToolRawMsgType
            tool_ref, msg = self._ws_recv_msg_queue.get()
            tool_msg = WSToolMsgParser().parse_tool_msg(msg)
            if isinstance(tool_msg, StatusInfo):
                tool_ref.update_status_info(tool_msg)
                logger.debug(
                    f"tool {tool_ref.name}#{tool_ref.uuid} status: {tool_ref.status.status if tool_ref.status is not None else 'UNKNOWN'}!"
                )
            elif isinstance(tool_msg, Result):
                logger.debug(
                    f"tool {tool_ref.name}#{tool_ref.uuid} got result: {tool_msg}"
                )
                self._results.put(tool_msg)
            elif isinstance(tool_msg, SchedulerCommandResponse):
                tool_ref.put_response(tool_msg)
            else:
                raise NotImplementedError(tool_msg)

    def _start_tasks(self):
        self._message_handling_thread.start()

    def start(self, debug=False):
        self._start_tasks()
        self.app.run(host=self.host, debug=debug, port=self.port)

    def start_in_thread(self):
        self.th = threading.Thread(target=self.start)
        self.th.setDaemon(True)
        self.th.start()
        logger.info("scheduler started!")
