import enum
import json
import os
import sys
from typing import Callable, Dict, Generator, List, Optional, Tuple, Union

from clang import cindex

from ...utils import MelodieGenerator

CompilerArgsType = Union[List[str], Callable[[str], List[str]]]


def parse_file(file: str, args: CompilerArgsType = None) -> cindex.TranslationUnit:
    """
    Open a c/cpp file, and return the corresponding translation unit

    :file: Name of file
    :args: Arguments to be passed into clang compiler, such as
        ``['-xc++', '-std=c++11']`` to analyse C++ 11 file.
    """
    if not os.path.exists(file):
        raise FileNotFoundError(file)
    index = cindex.Index.create()

    if args is None:
        return index.parse(file)
    elif isinstance(args, (list, tuple, set)):
        return index.parse(file, args=args)
    elif callable(args):
        return index.parse(file, args=args(file))
    else:
        raise NotImplementedError(f"Cannot recognize args {args}")


def get_func_decl(node: cindex.Cursor, func_name: str) -> Optional[cindex.Cursor]:
    """
    Get the function named `func_name` from Clang AST. If not exist, return None.
    """
    for node in node.get_children():
        if node.kind == cindex.CursorKind.FUNCTION_DECL:
            if node.spelling == func_name:
                return node
    return None


def is_function_definition(node: cindex.Cursor) -> bool:
    """
    Tell if this ``FUNCTION_DECL`` is definition (or only a declaration).
    """
    assert node.kind == cindex.CursorKind.FUNCTION_DECL
    child: cindex.Cursor
    is_definition = False
    for child in node.get_children():
        if child.kind == cindex.CursorKind.COMPOUND_STMT:
            is_definition = True
    return is_definition


def get_func_decl_all(
    node: cindex.Cursor, definition_only=False
) -> MelodieGenerator[cindex.Cursor]:
    """
    Get all function definitions from Clang AST.

    :definition_only: False by default. If true, this function will return functions with definitions
     only. Otherwise, this function will return both defined and declared functions
    """

    def _(node):
        for node in node.get_children():
            if node.kind == cindex.CursorKind.FUNCTION_DECL:
                if not definition_only or (
                    definition_only and is_function_definition(node)
                ):
                    yield node

    return MelodieGenerator(_(node))


class TraversalContext:
    """
    Used when traversing the Clang AST with recording the AST hierarchy information.
    """

    def __init__(self) -> None:
        self.hierarchy: List[cindex.Cursor] = []

    def print_hierarchy(self):
        print([c.kind for c in self.hierarchy])

    @property
    def current_node(self) -> cindex.Cursor:
        """
        Current node in the Clang AST
        """
        if len(self.hierarchy) > 0:
            return self.hierarchy[-1]
        else:
            raise ValueError("Traversal context does not contain any node.")

    def _push(self, node: cindex.Cursor):
        self.hierarchy.append(node)

    def _pop(self):
        self.hierarchy.pop()

    def find_by_kind(self, kind: cindex.CursorKind):
        """
        Search the AST hierarchy, get the AST node of the same kind.
        """
        for item in self.hierarchy:
            if item.kind == kind:
                return item
        return None

    def find_by_kind_td(self, kind: cindex.CursorKind):
        """
        Perform top-down search by AST node kind in the hierarchy.
        """
        for item in reversed(self.hierarchy):
            if item.kind == kind:
                return item
        return None

    def nearest_statement(self) -> Tuple[cindex.Cursor, cindex.Cursor]:
        """
        Find nearest Compound Statement

        :return:
        """
        compound_stmt: cindex.Cursor = None
        index = len(self.hierarchy)
        for item in reversed(self.hierarchy):
            index -= 1
            if item.kind in {cindex.CursorKind.COMPOUND_STMT}:
                compound_stmt = item
                break

        expr: cindex.Cursor = self.hierarchy[index + 1]  # compound_stmt下的
        return compound_stmt, expr

    def __len__(self):
        return len(self.hierarchy)


TraversalCallbackType = Callable[[TraversalContext], None]


def _traversal_with_callback(
    node: cindex.Cursor, ctx: TraversalContext, func: TraversalCallbackType
) -> None:
    for subnode in node.get_children():
        ctx._push(subnode)
        func(ctx)
        _traversal_with_callback(subnode, ctx, func)
        ctx._pop()
    return


def traversal_with_callback(node: cindex.Cursor, func: TraversalCallbackType):
    """
    Traverse the AST and for each node call `func` with callback
    """
    ctx = TraversalContext()
    ctx._push(node)
    func(ctx)
    _traversal_with_callback(node, ctx, func)
    ctx._pop()


def _traversal(
    node: cindex.Cursor, ctx: TraversalContext
) -> Generator[TraversalContext, None, None]:
    for subnode in node.get_children():
        ctx._push(subnode)
        yield ctx
        yield from _traversal(subnode, ctx)
        ctx._pop()
    return


def traversal(
    node: cindex.Cursor,
) -> MelodieGenerator[TraversalContext]:
    """
    Traverse the AST and for each node, returning a ``TraversalContext``.

    Unlike ``Cursor.walk_preorder()``, TraversalContext also contains hierarchical information
    in which block or branch the ``Cursor`` is.
    """

    def _(node):
        ctx = TraversalContext()
        ctx._push(node)
        yield ctx
        yield from _traversal(node, ctx)
        ctx._pop()

    return MelodieGenerator(_(node))


def iter_ast(node: cindex.Cursor) -> MelodieGenerator[cindex.Cursor]:
    """
    Iterate through all AST nodes
    """

    def _(node):
        yield from node.walk_preorder()

    return MelodieGenerator(_(node))


def iter_ast_from_file(
    file: str, args: CompilerArgsType = None
) -> MelodieGenerator[cindex.Cursor]:
    """
    Iterate through all AST nodes in file
    """
    node: cindex.Cursor = parse_file(file, args).cursor
    return iter_ast(node)


def split_binary_operator(
    node: cindex.Cursor,
) -> Tuple[cindex.Cursor, str, cindex.Cursor]:
    """
    Split binary operator.

    .. code-block:: python

        left, op, right = split_binary_operator(cursor)

    The result:
        * left: a Cursor object
        * right: a Cursor object
        * op:  a str, "+"

    """
    assert node.kind == cindex.CursorKind.BINARY_OPERATOR, node.kind
    children_iterator = node.get_children()
    left = next(children_iterator)
    symbol = list(node.get_tokens())[len(list(left.get_tokens()))].spelling
    right = next(children_iterator)
    return left, symbol, right


def split_compound_assignment(
    cursor: cindex.Cursor,
) -> Tuple[cindex.Cursor, str, cindex.Cursor]:
    """
    Split compound assignment to l_value_ast, operator and r_value_ast

    """
    l_value_ast, r_value_ast = list(cursor.get_children())
    lvalue_length = len(list(l_value_ast.get_tokens()))
    token: cindex.Token
    for i, token in enumerate(cursor.get_tokens()):
        if i == lvalue_length:
            break
    op = token.spelling
    return l_value_ast, op, r_value_ast


def split_for_loop_conditions(
    node: cindex.Cursor,
) -> Tuple[
    Optional[cindex.Cursor],
    Optional[cindex.Cursor],
    Optional[cindex.Cursor],
    Optional[cindex.Cursor],
]:
    """
    Split for loop conditions to handle omitted conditions.
    """
    splitter_positions: List[int] = []
    for tok in node.get_tokens():
        if tok.spelling == ";":
            loc: cindex.SourceLocation = tok.location
            splitter_positions.append(loc.offset)
        if len(splitter_positions) >= 2:
            if tok.spelling == ")":
                splitter_positions.append(tok.location.offset)
                break
    assert len(splitter_positions) == 3, splitter_positions
    parts: List[Optional[cindex.Cursor]] = [None, None, None, None]
    for child in node.get_children():
        if child.location.offset < splitter_positions[0]:
            parts[0] = child
        elif splitter_positions[0] <= child.location.offset < splitter_positions[1]:
            parts[1] = child
        elif splitter_positions[1] <= child.location.offset < splitter_positions[2]:
            parts[2] = child
        else:
            parts[3] = child
    return parts[0], parts[1], parts[2], parts[3]


class UnaryOpPos(enum.Enum):
    """
    A Enum standing for the positional relationship of unary operator
    and its target expression

    * BEFORE: Operator is before the expression, such as ``*p``, ``++i``
    * AFTER: Operator is after the expression, such as ``p++``
    """

    BEFORE = "before"
    AFTER = "after"


def split_unary_operator(
    node: cindex.Cursor,
) -> Tuple[str, cindex.Cursor, UnaryOpPos]:
    """
    Split unary operator

    :return: A tuple, (Unary Operator, operated expression, operator is before/after expression)
    """
    assert node.kind == cindex.CursorKind.UNARY_OPERATOR, node.kind
    node_tokens = "".join([t.spelling for t in node.get_tokens()])
    child = next(node.get_children())
    child_tokens = "".join([t.spelling for t in child.get_tokens()])
    if node_tokens.startswith(child_tokens):  # unary operator is after child expression
        return node_tokens[len(child_tokens) :], child, UnaryOpPos.AFTER
    else:
        return node_tokens[: -len(child_tokens)], child, UnaryOpPos.BEFORE


def get_compound_assignment_operator(node: cindex.Cursor) -> str:
    """
    get the symbol of COMPOUND_ASSIGNMENT_OPERATOR
    """
    assert node.kind == cindex.CursorKind.COMPOUND_ASSIGNMENT_OPERATOR, node.kind

    left = next(node.get_children())
    symbol = list(node.get_tokens())[len(list(left.get_tokens()))].spelling
    return symbol


def iter_files(
    folder: str,
    filetypes: Union[str, Tuple[str], Callable[[str], bool]] = "",
    abspath=True,
) -> MelodieGenerator[str]:
    """
    Iterate all files inside the folder.
    """
    if not callable(filetypes):
        if filetypes != "":

            def filter_func(s: str):
                return s.endswith(filetypes)

        else:

            def filter_func(s):
                return True

    else:
        filter_func = filetypes

    def _():
        for root, _, files in os.walk(folder):
            for file in files:
                if filter_func(file):
                    yield os.path.join(root, file) if abspath else file

    return MelodieGenerator(_())


def is_literal_kind(node: cindex.Cursor):
    return node.kind in {
        cindex.CursorKind.INTEGER_LITERAL,
        cindex.CursorKind.FLOATING_LITERAL,
        cindex.CursorKind.IMAGINARY_LITERAL,
        cindex.CursorKind.STRING_LITERAL,
        cindex.CursorKind.CHARACTER_LITERAL,
        cindex.CursorKind.CXX_BOOL_LITERAL_EXPR,
    }


def extract_literal_value(node: cindex.Cursor) -> Optional[str]:
    for node in node.walk_preorder():
        if is_literal_kind(node):
            tokens = list(node.get_tokens())
            if len(tokens) >= 1:
                return tokens[0].spelling
            else:
                return None


class ASTExtractor:
    def __init__(
        self, with_id: bool, type: bool, position: bool, with_kind_value: bool
    ):
        self.node_inc_id = 0
        self.with_id = with_id
        self.type = type
        self.position = position
        self.with_kind_value = with_kind_value

    def _ast_extract(self, node: cindex.Cursor, ast_struct: Dict):
        if self.with_id:
            ast_struct["id"] = self.node_inc_id

        has_kind = False
        # try:
        if self.with_kind_value:
            ast_struct["kind"] = node.kind.value
        ast_struct["kindText"] = str(node.kind)
        has_kind = True
        if self.position:
            ast_struct["position"] = (node.location.line, node.location.column)
        if self.type:
            try:
                node_type: cindex.Type = node.type
                ast_struct["type"] = {
                    "spelling": node_type.spelling,
                    "kind": str(node_type.kind),
                }
                if node_type.kind == cindex.TypeKind.POINTER:
                    pointee_type: cindex.Type = node_type.get_pointee()
                    ast_struct["type"]["pointee"] = str(pointee_type.spelling)
            except:
                import traceback

                traceback.print_exc()

        self.node_inc_id += 1

        # node may not be Cursor, but must have property `kind`, and method `get_children`
        if isinstance(node, cindex.Cursor):
            if node.spelling:
                ast_struct["spelling"] = node.spelling
            elif has_kind and is_literal_kind(node):
                # tokens = list(node.get_tokens())
                # if len(tokens) >= 1:
                # assert len(tokens) == 1, [t.spelling for t in tokens]
                # value = tokens[0].spelling
                # if node.kind == cindex.CursorKind.INTEGER_LITERAL:
                #     value = value
                # elif node.kind == cindex.CursorKind.FLOATING_LITERAL:
                #     value = value
                ast_struct["value"] = extract_literal_value(node)

        subnode: cindex.Cursor
        for subnode in node.get_children():
            if "children" not in ast_struct:
                ast_struct["children"] = []
            props = {}
            self._ast_extract(subnode, props)
            ast_struct["children"].append(props)

    def extract(self, node: cindex.Cursor):
        ast_root = {}
        self._ast_extract(node, ast_root)
        return ast_root


def extract_ast(
    node: cindex.Cursor,
    with_id=True,
    with_type=True,
    with_position=True,
    with_kind_value=True,
):
    """
    Convert a Clang-AST node to a JSON-Serializable Dict

    :with_id: If the dumped dict contains ID of AST node
    :with_type: If the dumped dict contains the data type of AST node
    :with_id: If the dumped dict contains Position of AST node
    :with_kind_value: If the dumped dict contains value of AST node
    """
    return ASTExtractor(with_id, with_type, with_position, with_kind_value).extract(
        node
    )


def beautified_print_ast(node: cindex.Cursor, filename=""):
    """
    Print Clang-AST with indented-JSON format

    :param filename:

        * If ``""``, print to stdout;
        * If provided a valid filename, write the JSON to the file.
    """
    if filename == "":
        file = sys.stdout
        print(json.dumps(extract_ast(node), indent=2), file=file)
    else:
        with open(filename, "w") as file:
            print(json.dumps(extract_ast(node), indent=2), file=file)


def print_tokens(node: cindex.Cursor) -> str:
    tokens = (token.spelling for token in node.get_tokens())
    return " ".join(tokens)


# def get_file_and_line(node: cindex.Cursor)->Tuple[str, int, int]:
#     # 获取源代码位置
#     location: cindex.SourceLocation = node.location

#     print(location)
#     # 获取文件名
#     file_name = cindex.conf.get_filename(location)

#     # 获取行号和列号
#     line = location.line
#     column = location.column

#     return file_name, line, column
