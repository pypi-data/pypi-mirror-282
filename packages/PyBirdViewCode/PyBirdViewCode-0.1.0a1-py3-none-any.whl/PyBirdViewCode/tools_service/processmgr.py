import signal
import subprocess
import sys
import threading
import time
from typing import Callable, Dict

import psutil
import logging

logger = logging.getLogger(__file__)

class SubprocessManager:
    _instance = None
    _sighandler = None
    processes: Dict[str, subprocess.Popen]

    def __init__(self, on_task_finish: Callable[[str], None]) -> None:
        self._sighandler = signal.signal(signal.SIGINT, self.on_sigint)
        self.processes = {}
        self.on_task_finish = on_task_finish
        self._bg_th = threading.Thread(target=self.task)
        self._bg_th.daemon = True
        self._bg_th.start()

    def start_subprocess(self, name: str, cmd: str, cwd: str):
        if name in self.processes:
            p = self.processes[name]
            if p.poll() is None:
                raise ValueError(f"Task named {name} is already running!")

        process = subprocess.Popen(cmd, cwd=cwd, shell=True)
        self.processes[name] = process

    def stop_subprocess(self, name):
        p = self.processes[name]
        process = psutil.Process(p.pid)
        for proc in process.children(recursive=True):
            proc.kill()
        process.kill()

    def on_sigint(self, sig, frame):
        for p in self.processes.values():
            if not p.poll():
                logger.info(f"command {p.args} terminated!")
                p.terminate()
        time.sleep(0.2)
        sys.exit(0)

    def task(self):
        while 1:
            stopped = []
            for task_name, p in self.processes.items():
                if p.poll() is not None:
                    stopped.append(task_name)
            for stopped_task in stopped:
                self.processes.pop(stopped_task)
                self.on_task_finish(stopped_task)
            time.sleep(0.5)
