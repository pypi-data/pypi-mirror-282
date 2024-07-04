import sys
import typing_extensions
from typing import Any, ClassVar, Generic, Literal, TypedDict, overload
from typing_extensions import Unpack

PyCF_ONLY_AST: Literal[1024]
PyCF_TYPE_COMMENTS: Literal[4096]
PyCF_ALLOW_TOP_LEVEL_AWAIT: Literal[8192]

if sys.version_info >= (3, 13):
    PyCF_OPTIMIZED_AST: Literal[33792]

# Used for node end positions in constructor keyword arguments
_EndPositionT = typing_extensions.TypeVar("_EndPositionT", int, int | None, default=int | None)

# Alias used for fields that must always be valid identifiers
# A string `x` counts as a valid identifier if both the following are True
# (1) `x.isidentifier()` evaluates to `True`
# (2) `keyword.iskeyword(x)` evaluates to `False`
_Identifier: typing_extensions.TypeAlias = str

# Corresponds to the names in the `_attributes` class variable which is non-empty in certain AST nodes
class _Attributes(TypedDict, Generic[_EndPositionT], total=False):
    lineno: int
    col_offset: int
    end_lineno: _EndPositionT
    end_col_offset: _EndPositionT

class AST:
    if sys.version_info >= (3, 10):
        __match_args__ = ()
    _attributes: ClassVar[tuple[str, ...]]
    _fields: ClassVar[tuple[str, ...]]
    if sys.version_info >= (3, 13):
        _field_types: ClassVar[dict[str, Any]]

class mod(AST):
    """
    mod = Module(stmt* body, type_ignore* type_ignores)
    | Interactive(stmt* body)
    | Expression(expr body)
    | FunctionType(expr* argtypes, expr returns)
    """
    ...
class type_ignore(AST):
    """type_ignore = TypeIgnore(int lineno, string tag)"""
    ...

class TypeIgnore(type_ignore):
    """TypeIgnore(int lineno, string tag)"""
    if sys.version_info >= (3, 10):
        __match_args__ = ("lineno", "tag")
    lineno: int
    tag: str
    def __init__(self, lineno: int, tag: str) -> None: ...

class FunctionType(mod):
    """FunctionType(expr* argtypes, expr returns)"""
    if sys.version_info >= (3, 10):
        __match_args__ = ("argtypes", "returns")
    argtypes: list[expr]
    returns: expr
    if sys.version_info >= (3, 13):
        @overload
        def __init__(self, argtypes: list[expr], returns: expr) -> None: ...
        @overload
        def __init__(self, argtypes: list[expr] = ..., *, returns: expr) -> None: ...
    else:
        def __init__(self, argtypes: list[expr], returns: expr) -> None: ...

class Module(mod):
    """Module(stmt* body, type_ignore* type_ignores)"""
    if sys.version_info >= (3, 10):
        __match_args__ = ("body", "type_ignores")
    body: list[stmt]
    type_ignores: list[TypeIgnore]
    if sys.version_info >= (3, 13):
        def __init__(self, body: list[stmt] = ..., type_ignores: list[TypeIgnore] = ...) -> None: ...
    else:
        def __init__(self, body: list[stmt], type_ignores: list[TypeIgnore]) -> None: ...

class Interactive(mod):
    """Interactive(stmt* body)"""
    if sys.version_info >= (3, 10):
        __match_args__ = ("body",)
    body: list[stmt]
    if sys.version_info >= (3, 13):
        def __init__(self, body: list[stmt] = ...) -> None: ...
    else:
        def __init__(self, body: list[stmt]) -> None: ...

class Expression(mod):
    """Expression(expr body)"""
    if sys.version_info >= (3, 10):
        __match_args__ = ("body",)
    body: expr
    def __init__(self, body: expr) -> None: ...

class stmt(AST):
    """
    stmt = FunctionDef(identifier name, arguments args, stmt* body, expr* decorator_list, expr? returns, string? type_comment)
    | AsyncFunctionDef(identifier name, arguments args, stmt* body, expr* decorator_list, expr? returns, string? type_comment)
    | ClassDef(identifier name, expr* bases, keyword* keywords, stmt* body, expr* decorator_list)
    | Return(expr? value)
    | Delete(expr* targets)
    | Assign(expr* targets, expr value, string? type_comment)
    | AugAssign(expr target, operator op, expr value)
    | AnnAssign(expr target, expr annotation, expr? value, int simple)
    | For(expr target, expr iter, stmt* body, stmt* orelse, string? type_comment)
    | AsyncFor(expr target, expr iter, stmt* body, stmt* orelse, string? type_comment)
    | While(expr test, stmt* body, stmt* orelse)
    | If(expr test, stmt* body, stmt* orelse)
    | With(withitem* items, stmt* body, string? type_comment)
    | AsyncWith(withitem* items, stmt* body, string? type_comment)
    | Raise(expr? exc, expr? cause)
    | Try(stmt* body, excepthandler* handlers, stmt* orelse, stmt* finalbody)
    | Assert(expr test, expr? msg)
    | Import(alias* names)
    | ImportFrom(identifier? module, alias* names, int? level)
    | Global(identifier* names)
    | Nonlocal(identifier* names)
    | Expr(expr value)
    | Pass
    | Break
    | Continue
    """
    lineno: int
    col_offset: int
    end_lineno: int | None
    end_col_offset: int | None
    def __init__(self, **kwargs: Unpack[_Attributes]) -> None: ...

class FunctionDef(stmt):
    """FunctionDef(identifier name, arguments args, stmt* body, expr* decorator_list, expr? returns, string? type_comment)"""
    if sys.version_info >= (3, 12):
        __match_args__ = ("name", "args", "body", "decorator_list", "returns", "type_comment", "type_params")
    elif sys.version_info >= (3, 10):
        __match_args__ = ("name", "args", "body", "decorator_list", "returns", "type_comment")
    name: _Identifier
    args: arguments
    body: list[stmt]
    decorator_list: list[expr]
    returns: expr | None
    type_comment: str | None
    if sys.version_info >= (3, 12):
        type_params: list[type_param]
    if sys.version_info >= (3, 13):
        def __init__(
            self,
            name: _Identifier,
            args: arguments,
            body: list[stmt] = ...,
            decorator_list: list[expr] = ...,
            returns: expr | None = None,
            type_comment: str | None = None,
            type_params: list[type_param] = ...,
            **kwargs: Unpack[_Attributes],
        ) -> None: ...
    elif sys.version_info >= (3, 12):
        @overload
        def __init__(
            self,
            name: _Identifier,
            args: arguments,
            body: list[stmt],
            decorator_list: list[expr],
            returns: expr | None,
            type_comment: str | None,
            type_params: list[type_param],
            **kwargs: Unpack[_Attributes],
        ) -> None: ...
        @overload
        def __init__(
            self,
            name: _Identifier,
            args: arguments,
            body: list[stmt],
            decorator_list: list[expr],
            returns: expr | None = None,
            type_comment: str | None = None,
            *,
            type_params: list[type_param],
            **kwargs: Unpack[_Attributes],
        ) -> None: ...
    else:
        def __init__(
            self,
            name: _Identifier,
            args: arguments,
            body: list[stmt],
            decorator_list: list[expr],
            returns: expr | None = None,
            type_comment: str | None = None,
            **kwargs: Unpack[_Attributes],
        ) -> None: ...

class AsyncFunctionDef(stmt):
    """AsyncFunctionDef(identifier name, arguments args, stmt* body, expr* decorator_list, expr? returns, string? type_comment)"""
    if sys.version_info >= (3, 12):
        __match_args__ = ("name", "args", "body", "decorator_list", "returns", "type_comment", "type_params")
    elif sys.version_info >= (3, 10):
        __match_args__ = ("name", "args", "body", "decorator_list", "returns", "type_comment")
    name: _Identifier
    args: arguments
    body: list[stmt]
    decorator_list: list[expr]
    returns: expr | None
    type_comment: str | None
    if sys.version_info >= (3, 12):
        type_params: list[type_param]
    if sys.version_info >= (3, 13):
        def __init__(
            self,
            name: _Identifier,
            args: arguments,
            body: list[stmt] = ...,
            decorator_list: list[expr] = ...,
            returns: expr | None = None,
            type_comment: str | None = None,
            type_params: list[type_param] = ...,
            **kwargs: Unpack[_Attributes],
        ) -> None: ...
    elif sys.version_info >= (3, 12):
        @overload
        def __init__(
            self,
            name: _Identifier,
            args: arguments,
            body: list[stmt],
            decorator_list: list[expr],
            returns: expr | None,
            type_comment: str | None,
            type_params: list[type_param],
            **kwargs: Unpack[_Attributes],
        ) -> None: ...
        @overload
        def __init__(
            self,
            name: _Identifier,
            args: arguments,
            body: list[stmt],
            decorator_list: list[expr],
            returns: expr | None = None,
            type_comment: str | None = None,
            *,
            type_params: list[type_param],
            **kwargs: Unpack[_Attributes],
        ) -> None: ...
    else:
        def __init__(
            self,
            name: _Identifier,
            args: arguments,
            body: list[stmt],
            decorator_list: list[expr],
            returns: expr | None = None,
            type_comment: str | None = None,
            **kwargs: Unpack[_Attributes],
        ) -> None: ...

class ClassDef(stmt):
    """ClassDef(identifier name, expr* bases, keyword* keywords, stmt* body, expr* decorator_list)"""
    if sys.version_info >= (3, 12):
        __match_args__ = ("name", "bases", "keywords", "body", "decorator_list", "type_params")
    elif sys.version_info >= (3, 10):
        __match_args__ = ("name", "bases", "keywords", "body", "decorator_list")
    name: _Identifier
    bases: list[expr]
    keywords: list[keyword]
    body: list[stmt]
    decorator_list: list[expr]
    if sys.version_info >= (3, 12):
        type_params: list[type_param]
    if sys.version_info >= (3, 13):
        def __init__(
            self,
            name: _Identifier,
            bases: list[expr] = ...,
            keywords: list[keyword] = ...,
            body: list[stmt] = ...,
            decorator_list: list[expr] = ...,
            type_params: list[type_param] = ...,
            **kwargs: Unpack[_Attributes],
        ) -> None: ...
    elif sys.version_info >= (3, 12):
        def __init__(
            self,
            name: _Identifier,
            bases: list[expr],
            keywords: list[keyword],
            body: list[stmt],
            decorator_list: list[expr],
            type_params: list[type_param],
            **kwargs: Unpack[_Attributes],
        ) -> None: ...
    else:
        def __init__(
            self,
            name: _Identifier,
            bases: list[expr],
            keywords: list[keyword],
            body: list[stmt],
            decorator_list: list[expr],
            **kwargs: Unpack[_Attributes],
        ) -> None: ...

class Return(stmt):
    """Return(expr? value)"""
    if sys.version_info >= (3, 10):
        __match_args__ = ("value",)
    value: expr | None
    def __init__(self, value: expr | None = None, **kwargs: Unpack[_Attributes]) -> None: ...

class Delete(stmt):
    """Delete(expr* targets)"""
    if sys.version_info >= (3, 10):
        __match_args__ = ("targets",)
    targets: list[expr]
    if sys.version_info >= (3, 13):
        def __init__(self, targets: list[expr] = ..., **kwargs: Unpack[_Attributes]) -> None: ...
    else:
        def __init__(self, targets: list[expr], **kwargs: Unpack[_Attributes]) -> None: ...

class Assign(stmt):
    """Assign(expr* targets, expr value, string? type_comment)"""
    if sys.version_info >= (3, 10):
        __match_args__ = ("targets", "value", "type_comment")
    targets: list[expr]
    value: expr
    type_comment: str | None
    if sys.version_info >= (3, 13):
        @overload
        def __init__(
            self, targets: list[expr], value: expr, type_comment: str | None = None, **kwargs: Unpack[_Attributes]
        ) -> None: ...
        @overload
        def __init__(
            self, targets: list[expr] = ..., *, value: expr, type_comment: str | None = None, **kwargs: Unpack[_Attributes]
        ) -> None: ...
    else:
        def __init__(
            self, targets: list[expr], value: expr, type_comment: str | None = None, **kwargs: Unpack[_Attributes]
        ) -> None: ...

class AugAssign(stmt):
    """AugAssign(expr target, operator op, expr value)"""
    if sys.version_info >= (3, 10):
        __match_args__ = ("target", "op", "value")
    target: Name | Attribute | Subscript
    op: operator
    value: expr
    def __init__(
        self, target: Name | Attribute | Subscript, op: operator, value: expr, **kwargs: Unpack[_Attributes]
    ) -> None: ...

class AnnAssign(stmt):
    """AnnAssign(expr target, expr annotation, expr? value, int simple)"""
    if sys.version_info >= (3, 10):
        __match_args__ = ("target", "annotation", "value", "simple")
    target: Name | Attribute | Subscript
    annotation: expr
    value: expr | None
    simple: int
    @overload
    def __init__(
        self,
        target: Name | Attribute | Subscript,
        annotation: expr,
        value: expr | None,
        simple: int,
        **kwargs: Unpack[_Attributes],
    ) -> None: ...
    @overload
    def __init__(
        self,
        target: Name | Attribute | Subscript,
        annotation: expr,
        value: expr | None = None,
        *,
        simple: int,
        **kwargs: Unpack[_Attributes],
    ) -> None: ...

class For(stmt):
    """For(expr target, expr iter, stmt* body, stmt* orelse, string? type_comment)"""
    if sys.version_info >= (3, 10):
        __match_args__ = ("target", "iter", "body", "orelse", "type_comment")
    target: expr
    iter: expr
    body: list[stmt]
    orelse: list[stmt]
    type_comment: str | None
    if sys.version_info >= (3, 13):
        def __init__(
            self,
            target: expr,
            iter: expr,
            body: list[stmt] = ...,
            orelse: list[stmt] = ...,
            type_comment: str | None = None,
            **kwargs: Unpack[_Attributes],
        ) -> None: ...
    else:
        def __init__(
            self,
            target: expr,
            iter: expr,
            body: list[stmt],
            orelse: list[stmt],
            type_comment: str | None = None,
            **kwargs: Unpack[_Attributes],
        ) -> None: ...

class AsyncFor(stmt):
    """AsyncFor(expr target, expr iter, stmt* body, stmt* orelse, string? type_comment)"""
    if sys.version_info >= (3, 10):
        __match_args__ = ("target", "iter", "body", "orelse", "type_comment")
    target: expr
    iter: expr
    body: list[stmt]
    orelse: list[stmt]
    type_comment: str | None
    if sys.version_info >= (3, 13):
        def __init__(
            self,
            target: expr,
            iter: expr,
            body: list[stmt] = ...,
            orelse: list[stmt] = ...,
            type_comment: str | None = None,
            **kwargs: Unpack[_Attributes],
        ) -> None: ...
    else:
        def __init__(
            self,
            target: expr,
            iter: expr,
            body: list[stmt],
            orelse: list[stmt],
            type_comment: str | None = None,
            **kwargs: Unpack[_Attributes],
        ) -> None: ...

class While(stmt):
    """While(expr test, stmt* body, stmt* orelse)"""
    if sys.version_info >= (3, 10):
        __match_args__ = ("test", "body", "orelse")
    test: expr
    body: list[stmt]
    orelse: list[stmt]
    if sys.version_info >= (3, 13):
        def __init__(
            self, test: expr, body: list[stmt] = ..., orelse: list[stmt] = ..., **kwargs: Unpack[_Attributes]
        ) -> None: ...
    else:
        def __init__(self, test: expr, body: list[stmt], orelse: list[stmt], **kwargs: Unpack[_Attributes]) -> None: ...

class If(stmt):
    """If(expr test, stmt* body, stmt* orelse)"""
    if sys.version_info >= (3, 10):
        __match_args__ = ("test", "body", "orelse")
    test: expr
    body: list[stmt]
    orelse: list[stmt]
    if sys.version_info >= (3, 13):
        def __init__(
            self, test: expr, body: list[stmt] = ..., orelse: list[stmt] = ..., **kwargs: Unpack[_Attributes]
        ) -> None: ...
    else:
        def __init__(self, test: expr, body: list[stmt], orelse: list[stmt], **kwargs: Unpack[_Attributes]) -> None: ...

class With(stmt):
    """With(withitem* items, stmt* body, string? type_comment)"""
    if sys.version_info >= (3, 10):
        __match_args__ = ("items", "body", "type_comment")
    items: list[withitem]
    body: list[stmt]
    type_comment: str | None
    if sys.version_info >= (3, 13):
        def __init__(
            self,
            items: list[withitem] = ...,
            body: list[stmt] = ...,
            type_comment: str | None = None,
            **kwargs: Unpack[_Attributes],
        ) -> None: ...
    else:
        def __init__(
            self, items: list[withitem], body: list[stmt], type_comment: str | None = None, **kwargs: Unpack[_Attributes]
        ) -> None: ...

class AsyncWith(stmt):
    """AsyncWith(withitem* items, stmt* body, string? type_comment)"""
    if sys.version_info >= (3, 10):
        __match_args__ = ("items", "body", "type_comment")
    items: list[withitem]
    body: list[stmt]
    type_comment: str | None
    if sys.version_info >= (3, 13):
        def __init__(
            self,
            items: list[withitem] = ...,
            body: list[stmt] = ...,
            type_comment: str | None = None,
            **kwargs: Unpack[_Attributes],
        ) -> None: ...
    else:
        def __init__(
            self, items: list[withitem], body: list[stmt], type_comment: str | None = None, **kwargs: Unpack[_Attributes]
        ) -> None: ...

class Raise(stmt):
    """Raise(expr? exc, expr? cause)"""
    if sys.version_info >= (3, 10):
        __match_args__ = ("exc", "cause")
    exc: expr | None
    cause: expr | None
    def __init__(self, exc: expr | None = None, cause: expr | None = None, **kwargs: Unpack[_Attributes]) -> None: ...

class Try(stmt):
    """Try(stmt* body, excepthandler* handlers, stmt* orelse, stmt* finalbody)"""
    if sys.version_info >= (3, 10):
        __match_args__ = ("body", "handlers", "orelse", "finalbody")
    body: list[stmt]
    handlers: list[ExceptHandler]
    orelse: list[stmt]
    finalbody: list[stmt]
    if sys.version_info >= (3, 13):
        def __init__(
            self,
            body: list[stmt] = ...,
            handlers: list[ExceptHandler] = ...,
            orelse: list[stmt] = ...,
            finalbody: list[stmt] = ...,
            **kwargs: Unpack[_Attributes],
        ) -> None: ...
    else:
        def __init__(
            self,
            body: list[stmt],
            handlers: list[ExceptHandler],
            orelse: list[stmt],
            finalbody: list[stmt],
            **kwargs: Unpack[_Attributes],
        ) -> None: ...

if sys.version_info >= (3, 11):
    class TryStar(stmt):
        """TryStar(stmt* body, excepthandler* handlers, stmt* orelse, stmt* finalbody)"""
        __match_args__ = ("body", "handlers", "orelse", "finalbody")
        body: list[stmt]
        handlers: list[ExceptHandler]
        orelse: list[stmt]
        finalbody: list[stmt]
        if sys.version_info >= (3, 13):
            def __init__(
                self,
                body: list[stmt] = ...,
                handlers: list[ExceptHandler] = ...,
                orelse: list[stmt] = ...,
                finalbody: list[stmt] = ...,
                **kwargs: Unpack[_Attributes],
            ) -> None: ...
        else:
            def __init__(
                self,
                body: list[stmt],
                handlers: list[ExceptHandler],
                orelse: list[stmt],
                finalbody: list[stmt],
                **kwargs: Unpack[_Attributes],
            ) -> None: ...

class Assert(stmt):
    """Assert(expr test, expr? msg)"""
    if sys.version_info >= (3, 10):
        __match_args__ = ("test", "msg")
    test: expr
    msg: expr | None
    def __init__(self, test: expr, msg: expr | None = None, **kwargs: Unpack[_Attributes]) -> None: ...

class Import(stmt):
    """Import(alias* names)"""
    if sys.version_info >= (3, 10):
        __match_args__ = ("names",)
    names: list[alias]
    if sys.version_info >= (3, 13):
        def __init__(self, names: list[alias] = ..., **kwargs: Unpack[_Attributes]) -> None: ...
    else:
        def __init__(self, names: list[alias], **kwargs: Unpack[_Attributes]) -> None: ...

class ImportFrom(stmt):
    """ImportFrom(identifier? module, alias* names, int? level)"""
    if sys.version_info >= (3, 10):
        __match_args__ = ("module", "names", "level")
    module: str | None
    names: list[alias]
    level: int
    if sys.version_info >= (3, 13):
        @overload
        def __init__(self, module: str | None, names: list[alias], level: int, **kwargs: Unpack[_Attributes]) -> None: ...
        @overload
        def __init__(
            self, module: str | None = None, names: list[alias] = ..., *, level: int, **kwargs: Unpack[_Attributes]
        ) -> None: ...
    else:
        @overload
        def __init__(self, module: str | None, names: list[alias], level: int, **kwargs: Unpack[_Attributes]) -> None: ...
        @overload
        def __init__(
            self, module: str | None = None, *, names: list[alias], level: int, **kwargs: Unpack[_Attributes]
        ) -> None: ...

class Global(stmt):
    """Global(identifier* names)"""
    if sys.version_info >= (3, 10):
        __match_args__ = ("names",)
    names: list[_Identifier]
    if sys.version_info >= (3, 13):
        def __init__(self, names: list[_Identifier] = ..., **kwargs: Unpack[_Attributes]) -> None: ...
    else:
        def __init__(self, names: list[_Identifier], **kwargs: Unpack[_Attributes]) -> None: ...

class Nonlocal(stmt):
    """Nonlocal(identifier* names)"""
    if sys.version_info >= (3, 10):
        __match_args__ = ("names",)
    names: list[_Identifier]
    if sys.version_info >= (3, 13):
        def __init__(self, names: list[_Identifier] = ..., **kwargs: Unpack[_Attributes]) -> None: ...
    else:
        def __init__(self, names: list[_Identifier], **kwargs: Unpack[_Attributes]) -> None: ...

class Expr(stmt):
    """Expr(expr value)"""
    if sys.version_info >= (3, 10):
        __match_args__ = ("value",)
    value: expr
    def __init__(self, value: expr, **kwargs: Unpack[_Attributes]) -> None: ...

class Pass(stmt):
    """Pass"""
    ...
class Break(stmt):
    """Break"""
    ...
class Continue(stmt):
    """Continue"""
    ...

class expr(AST):
    """
    expr = BoolOp(boolop op, expr* values)
    | NamedExpr(expr target, expr value)
    | BinOp(expr left, operator op, expr right)
    | UnaryOp(unaryop op, expr operand)
    | Lambda(arguments args, expr body)
    | IfExp(expr test, expr body, expr orelse)
    | Dict(expr* keys, expr* values)
    | Set(expr* elts)
    | ListComp(expr elt, comprehension* generators)
    | SetComp(expr elt, comprehension* generators)
    | DictComp(expr key, expr value, comprehension* generators)
    | GeneratorExp(expr elt, comprehension* generators)
    | Await(expr value)
    | Yield(expr? value)
    | YieldFrom(expr value)
    | Compare(expr left, cmpop* ops, expr* comparators)
    | Call(expr func, expr* args, keyword* keywords)
    | FormattedValue(expr value, int? conversion, expr? format_spec)
    | JoinedStr(expr* values)
    | Constant(constant value, string? kind)
    | Attribute(expr value, identifier attr, expr_context ctx)
    | Subscript(expr value, expr slice, expr_context ctx)
    | Starred(expr value, expr_context ctx)
    | Name(identifier id, expr_context ctx)
    | List(expr* elts, expr_context ctx)
    | Tuple(expr* elts, expr_context ctx)
    | Slice(expr? lower, expr? upper, expr? step)
    """
    lineno: int
    col_offset: int
    end_lineno: int | None
    end_col_offset: int | None
    def __init__(self, **kwargs: Unpack[_Attributes]) -> None: ...

class BoolOp(expr):
    """BoolOp(boolop op, expr* values)"""
    if sys.version_info >= (3, 10):
        __match_args__ = ("op", "values")
    op: boolop
    values: list[expr]
    if sys.version_info >= (3, 13):
        def __init__(self, op: boolop, values: list[expr] = ..., **kwargs: Unpack[_Attributes]) -> None: ...
    else:
        def __init__(self, op: boolop, values: list[expr], **kwargs: Unpack[_Attributes]) -> None: ...

class BinOp(expr):
    """BinOp(expr left, operator op, expr right)"""
    if sys.version_info >= (3, 10):
        __match_args__ = ("left", "op", "right")
    left: expr
    op: operator
    right: expr
    def __init__(self, left: expr, op: operator, right: expr, **kwargs: Unpack[_Attributes]) -> None: ...

class UnaryOp(expr):
    """UnaryOp(unaryop op, expr operand)"""
    if sys.version_info >= (3, 10):
        __match_args__ = ("op", "operand")
    op: unaryop
    operand: expr
    def __init__(self, op: unaryop, operand: expr, **kwargs: Unpack[_Attributes]) -> None: ...

class Lambda(expr):
    """Lambda(arguments args, expr body)"""
    if sys.version_info >= (3, 10):
        __match_args__ = ("args", "body")
    args: arguments
    body: expr
    def __init__(self, args: arguments, body: expr, **kwargs: Unpack[_Attributes]) -> None: ...

class IfExp(expr):
    """IfExp(expr test, expr body, expr orelse)"""
    if sys.version_info >= (3, 10):
        __match_args__ = ("test", "body", "orelse")
    test: expr
    body: expr
    orelse: expr
    def __init__(self, test: expr, body: expr, orelse: expr, **kwargs: Unpack[_Attributes]) -> None: ...

class Dict(expr):
    """Dict(expr* keys, expr* values)"""
    if sys.version_info >= (3, 10):
        __match_args__ = ("keys", "values")
    keys: list[expr | None]
    values: list[expr]
    if sys.version_info >= (3, 13):
        def __init__(self, keys: list[expr | None] = ..., values: list[expr] = ..., **kwargs: Unpack[_Attributes]) -> None: ...
    else:
        def __init__(self, keys: list[expr | None], values: list[expr], **kwargs: Unpack[_Attributes]) -> None: ...

class Set(expr):
    """Set(expr* elts)"""
    if sys.version_info >= (3, 10):
        __match_args__ = ("elts",)
    elts: list[expr]
    if sys.version_info >= (3, 13):
        def __init__(self, elts: list[expr] = ..., **kwargs: Unpack[_Attributes]) -> None: ...
    else:
        def __init__(self, elts: list[expr], **kwargs: Unpack[_Attributes]) -> None: ...

class ListComp(expr):
    """ListComp(expr elt, comprehension* generators)"""
    if sys.version_info >= (3, 10):
        __match_args__ = ("elt", "generators")
    elt: expr
    generators: list[comprehension]
    if sys.version_info >= (3, 13):
        def __init__(self, elt: expr, generators: list[comprehension] = ..., **kwargs: Unpack[_Attributes]) -> None: ...
    else:
        def __init__(self, elt: expr, generators: list[comprehension], **kwargs: Unpack[_Attributes]) -> None: ...

class SetComp(expr):
    """SetComp(expr elt, comprehension* generators)"""
    if sys.version_info >= (3, 10):
        __match_args__ = ("elt", "generators")
    elt: expr
    generators: list[comprehension]
    if sys.version_info >= (3, 13):
        def __init__(self, elt: expr, generators: list[comprehension] = ..., **kwargs: Unpack[_Attributes]) -> None: ...
    else:
        def __init__(self, elt: expr, generators: list[comprehension], **kwargs: Unpack[_Attributes]) -> None: ...

class DictComp(expr):
    """DictComp(expr key, expr value, comprehension* generators)"""
    if sys.version_info >= (3, 10):
        __match_args__ = ("key", "value", "generators")
    key: expr
    value: expr
    generators: list[comprehension]
    if sys.version_info >= (3, 13):
        def __init__(
            self, key: expr, value: expr, generators: list[comprehension] = ..., **kwargs: Unpack[_Attributes]
        ) -> None: ...
    else:
        def __init__(self, key: expr, value: expr, generators: list[comprehension], **kwargs: Unpack[_Attributes]) -> None: ...

class GeneratorExp(expr):
    """GeneratorExp(expr elt, comprehension* generators)"""
    if sys.version_info >= (3, 10):
        __match_args__ = ("elt", "generators")
    elt: expr
    generators: list[comprehension]
    if sys.version_info >= (3, 13):
        def __init__(self, elt: expr, generators: list[comprehension] = ..., **kwargs: Unpack[_Attributes]) -> None: ...
    else:
        def __init__(self, elt: expr, generators: list[comprehension], **kwargs: Unpack[_Attributes]) -> None: ...

class Await(expr):
    """Await(expr value)"""
    if sys.version_info >= (3, 10):
        __match_args__ = ("value",)
    value: expr
    def __init__(self, value: expr, **kwargs: Unpack[_Attributes]) -> None: ...

class Yield(expr):
    """Yield(expr? value)"""
    if sys.version_info >= (3, 10):
        __match_args__ = ("value",)
    value: expr | None
    def __init__(self, value: expr | None = None, **kwargs: Unpack[_Attributes]) -> None: ...

class YieldFrom(expr):
    """YieldFrom(expr value)"""
    if sys.version_info >= (3, 10):
        __match_args__ = ("value",)
    value: expr
    def __init__(self, value: expr, **kwargs: Unpack[_Attributes]) -> None: ...

class Compare(expr):
    """Compare(expr left, cmpop* ops, expr* comparators)"""
    if sys.version_info >= (3, 10):
        __match_args__ = ("left", "ops", "comparators")
    left: expr
    ops: list[cmpop]
    comparators: list[expr]
    if sys.version_info >= (3, 13):
        def __init__(
            self, left: expr, ops: list[cmpop] = ..., comparators: list[expr] = ..., **kwargs: Unpack[_Attributes]
        ) -> None: ...
    else:
        def __init__(self, left: expr, ops: list[cmpop], comparators: list[expr], **kwargs: Unpack[_Attributes]) -> None: ...

class Call(expr):
    """Call(expr func, expr* args, keyword* keywords)"""
    if sys.version_info >= (3, 10):
        __match_args__ = ("func", "args", "keywords")
    func: expr
    args: list[expr]
    keywords: list[keyword]
    if sys.version_info >= (3, 13):
        def __init__(
            self, func: expr, args: list[expr] = ..., keywords: list[keyword] = ..., **kwargs: Unpack[_Attributes]
        ) -> None: ...
    else:
        def __init__(self, func: expr, args: list[expr], keywords: list[keyword], **kwargs: Unpack[_Attributes]) -> None: ...

class FormattedValue(expr):
    """FormattedValue(expr value, int? conversion, expr? format_spec)"""
    if sys.version_info >= (3, 10):
        __match_args__ = ("value", "conversion", "format_spec")
    value: expr
    conversion: int
    format_spec: expr | None
    def __init__(self, value: expr, conversion: int, format_spec: expr | None = None, **kwargs: Unpack[_Attributes]) -> None: ...

class JoinedStr(expr):
    """JoinedStr(expr* values)"""
    if sys.version_info >= (3, 10):
        __match_args__ = ("values",)
    values: list[expr]
    if sys.version_info >= (3, 13):
        def __init__(self, values: list[expr] = ..., **kwargs: Unpack[_Attributes]) -> None: ...
    else:
        def __init__(self, values: list[expr], **kwargs: Unpack[_Attributes]) -> None: ...

class Constant(expr):
    """Constant(constant value, string? kind)"""
    if sys.version_info >= (3, 10):
        __match_args__ = ("value", "kind")
    value: Any  # None, str, bytes, bool, int, float, complex, Ellipsis
    kind: str | None
    # Aliases for value, for backwards compatibility
    s: Any
    n: int | float | complex
    def __init__(self, value: Any, kind: str | None = None, **kwargs: Unpack[_Attributes]) -> None: ...

class NamedExpr(expr):
    """NamedExpr(expr target, expr value)"""
    if sys.version_info >= (3, 10):
        __match_args__ = ("target", "value")
    target: Name
    value: expr
    def __init__(self, target: Name, value: expr, **kwargs: Unpack[_Attributes]) -> None: ...

class Attribute(expr):
    """Attribute(expr value, identifier attr, expr_context ctx)"""
    if sys.version_info >= (3, 10):
        __match_args__ = ("value", "attr", "ctx")
    value: expr
    attr: _Identifier
    ctx: expr_context  # Not present in Python < 3.13 if not passed to `__init__`
    def __init__(self, value: expr, attr: _Identifier, ctx: expr_context = ..., **kwargs: Unpack[_Attributes]) -> None: ...

if sys.version_info >= (3, 9):
    _Slice: typing_extensions.TypeAlias = expr
    _SliceAttributes: typing_extensions.TypeAlias = _Attributes
else:
    class slice(AST): ...
    _Slice: typing_extensions.TypeAlias = slice

    class _SliceAttributes(TypedDict): ...

class Slice(_Slice):
    """Slice(expr? lower, expr? upper, expr? step)"""
    if sys.version_info >= (3, 10):
        __match_args__ = ("lower", "upper", "step")
    lower: expr | None
    upper: expr | None
    step: expr | None
    def __init__(
        self, lower: expr | None = None, upper: expr | None = None, step: expr | None = None, **kwargs: Unpack[_SliceAttributes]
    ) -> None: ...

if sys.version_info < (3, 9):
    class ExtSlice(slice):
        dims: list[slice]
        def __init__(self, dims: list[slice], **kwargs: Unpack[_SliceAttributes]) -> None: ...

    class Index(slice):
        value: expr
        def __init__(self, value: expr, **kwargs: Unpack[_SliceAttributes]) -> None: ...

class Subscript(expr):
    """Subscript(expr value, expr slice, expr_context ctx)"""
    if sys.version_info >= (3, 10):
        __match_args__ = ("value", "slice", "ctx")
    value: expr
    slice: _Slice
    ctx: expr_context  # Not present in Python < 3.13 if not passed to `__init__`
    def __init__(self, value: expr, slice: _Slice, ctx: expr_context = ..., **kwargs: Unpack[_Attributes]) -> None: ...

class Starred(expr):
    """Starred(expr value, expr_context ctx)"""
    if sys.version_info >= (3, 10):
        __match_args__ = ("value", "ctx")
    value: expr
    ctx: expr_context  # Not present in Python < 3.13 if not passed to `__init__`
    def __init__(self, value: expr, ctx: expr_context = ..., **kwargs: Unpack[_Attributes]) -> None: ...

class Name(expr):
    """Name(identifier id, expr_context ctx)"""
    if sys.version_info >= (3, 10):
        __match_args__ = ("id", "ctx")
    id: _Identifier
    ctx: expr_context  # Not present in Python < 3.13 if not passed to `__init__`
    def __init__(self, id: _Identifier, ctx: expr_context = ..., **kwargs: Unpack[_Attributes]) -> None: ...

class List(expr):
    """List(expr* elts, expr_context ctx)"""
    if sys.version_info >= (3, 10):
        __match_args__ = ("elts", "ctx")
    elts: list[expr]
    ctx: expr_context  # Not present in Python < 3.13 if not passed to `__init__`
    if sys.version_info >= (3, 13):
        def __init__(self, elts: list[expr] = ..., ctx: expr_context = ..., **kwargs: Unpack[_Attributes]) -> None: ...
    else:
        def __init__(self, elts: list[expr], ctx: expr_context = ..., **kwargs: Unpack[_Attributes]) -> None: ...

class Tuple(expr):
    """Tuple(expr* elts, expr_context ctx)"""
    if sys.version_info >= (3, 10):
        __match_args__ = ("elts", "ctx")
    elts: list[expr]
    ctx: expr_context  # Not present in Python < 3.13 if not passed to `__init__`
    if sys.version_info >= (3, 9):
        dims: list[expr]
    if sys.version_info >= (3, 13):
        def __init__(self, elts: list[expr] = ..., ctx: expr_context = ..., **kwargs: Unpack[_Attributes]) -> None: ...
    else:
        def __init__(self, elts: list[expr], ctx: expr_context = ..., **kwargs: Unpack[_Attributes]) -> None: ...

class expr_context(AST):
    """expr_context = Load | Store | Del"""
    ...

if sys.version_info < (3, 9):
    class AugLoad(expr_context): ...
    class AugStore(expr_context): ...
    class Param(expr_context): ...

    class Suite(mod):
        body: list[stmt]
        def __init__(self, body: list[stmt]) -> None: ...

class Del(expr_context):
    """Del"""
    ...
class Load(expr_context):
    """Load"""
    ...
class Store(expr_context):
    """Store"""
    ...
class boolop(AST):
    """boolop = And | Or"""
    ...
class And(boolop):
    """And"""
    ...
class Or(boolop):
    """Or"""
    ...
class operator(AST):
    """operator = Add | Sub | Mult | MatMult | Div | Mod | Pow | LShift | RShift | BitOr | BitXor | BitAnd | FloorDiv"""
    ...
class Add(operator):
    """Add"""
    ...
class BitAnd(operator):
    """BitAnd"""
    ...
class BitOr(operator):
    """BitOr"""
    ...
class BitXor(operator):
    """BitXor"""
    ...
class Div(operator):
    """Div"""
    ...
class FloorDiv(operator):
    """FloorDiv"""
    ...
class LShift(operator):
    """LShift"""
    ...
class Mod(operator):
    """Mod"""
    ...
class Mult(operator):
    """Mult"""
    ...
class MatMult(operator):
    """MatMult"""
    ...
class Pow(operator):
    """Pow"""
    ...
class RShift(operator):
    """RShift"""
    ...
class Sub(operator):
    """Sub"""
    ...
class unaryop(AST):
    """unaryop = Invert | Not | UAdd | USub"""
    ...
class Invert(unaryop):
    """Invert"""
    ...
class Not(unaryop):
    """Not"""
    ...
class UAdd(unaryop):
    """UAdd"""
    ...
class USub(unaryop):
    """USub"""
    ...
class cmpop(AST):
    """cmpop = Eq | NotEq | Lt | LtE | Gt | GtE | Is | IsNot | In | NotIn"""
    ...
class Eq(cmpop):
    """Eq"""
    ...
class Gt(cmpop):
    """Gt"""
    ...
class GtE(cmpop):
    """GtE"""
    ...
class In(cmpop):
    """In"""
    ...
class Is(cmpop):
    """Is"""
    ...
class IsNot(cmpop):
    """IsNot"""
    ...
class Lt(cmpop):
    """Lt"""
    ...
class LtE(cmpop):
    """LtE"""
    ...
class NotEq(cmpop):
    """NotEq"""
    ...
class NotIn(cmpop):
    """NotIn"""
    ...

class comprehension(AST):
    """comprehension(expr target, expr iter, expr* ifs, int is_async)"""
    if sys.version_info >= (3, 10):
        __match_args__ = ("target", "iter", "ifs", "is_async")
    target: expr
    iter: expr
    ifs: list[expr]
    is_async: int
    if sys.version_info >= (3, 13):
        @overload
        def __init__(self, target: expr, iter: expr, ifs: list[expr], is_async: int) -> None: ...
        @overload
        def __init__(self, target: expr, iter: expr, ifs: list[expr] = ..., *, is_async: int) -> None: ...
    else:
        def __init__(self, target: expr, iter: expr, ifs: list[expr], is_async: int) -> None: ...

class excepthandler(AST):
    """excepthandler = ExceptHandler(expr? type, identifier? name, stmt* body)"""
    lineno: int
    col_offset: int
    end_lineno: int | None
    end_col_offset: int | None
    def __init__(self, **kwargs: Unpack[_Attributes]) -> None: ...

class ExceptHandler(excepthandler):
    """ExceptHandler(expr? type, identifier? name, stmt* body)"""
    if sys.version_info >= (3, 10):
        __match_args__ = ("type", "name", "body")
    type: expr | None
    name: _Identifier | None
    body: list[stmt]
    if sys.version_info >= (3, 13):
        def __init__(
            self, type: expr | None = None, name: _Identifier | None = None, body: list[stmt] = ..., **kwargs: Unpack[_Attributes]
        ) -> None: ...
    else:
        @overload
        def __init__(
            self, type: expr | None, name: _Identifier | None, body: list[stmt], **kwargs: Unpack[_Attributes]
        ) -> None: ...
        @overload
        def __init__(
            self, type: expr | None = None, name: _Identifier | None = None, *, body: list[stmt], **kwargs: Unpack[_Attributes]
        ) -> None: ...

class arguments(AST):
    """arguments(arg* posonlyargs, arg* args, arg? vararg, arg* kwonlyargs, expr* kw_defaults, arg? kwarg, expr* defaults)"""
    if sys.version_info >= (3, 10):
        __match_args__ = ("posonlyargs", "args", "vararg", "kwonlyargs", "kw_defaults", "kwarg", "defaults")
    posonlyargs: list[arg]
    args: list[arg]
    vararg: arg | None
    kwonlyargs: list[arg]
    kw_defaults: list[expr | None]
    kwarg: arg | None
    defaults: list[expr]
    if sys.version_info >= (3, 13):
        def __init__(
            self,
            posonlyargs: list[arg] = ...,
            args: list[arg] = ...,
            vararg: arg | None = None,
            kwonlyargs: list[arg] = ...,
            kw_defaults: list[expr | None] = ...,
            kwarg: arg | None = None,
            defaults: list[expr] = ...,
        ) -> None: ...
    else:
        @overload
        def __init__(
            self,
            posonlyargs: list[arg],
            args: list[arg],
            vararg: arg | None,
            kwonlyargs: list[arg],
            kw_defaults: list[expr | None],
            kwarg: arg | None,
            defaults: list[expr],
        ) -> None: ...
        @overload
        def __init__(
            self,
            posonlyargs: list[arg],
            args: list[arg],
            vararg: arg | None,
            kwonlyargs: list[arg],
            kw_defaults: list[expr | None],
            kwarg: arg | None = None,
            *,
            defaults: list[expr],
        ) -> None: ...
        @overload
        def __init__(
            self,
            posonlyargs: list[arg],
            args: list[arg],
            vararg: arg | None = None,
            *,
            kwonlyargs: list[arg],
            kw_defaults: list[expr | None],
            kwarg: arg | None = None,
            defaults: list[expr],
        ) -> None: ...

class arg(AST):
    """arg(identifier arg, expr? annotation, string? type_comment)"""
    lineno: int
    col_offset: int
    end_lineno: int | None
    end_col_offset: int | None
    if sys.version_info >= (3, 10):
        __match_args__ = ("arg", "annotation", "type_comment")
    arg: _Identifier
    annotation: expr | None
    type_comment: str | None
    def __init__(
        self, arg: _Identifier, annotation: expr | None = None, type_comment: str | None = None, **kwargs: Unpack[_Attributes]
    ) -> None: ...

class keyword(AST):
    """keyword(identifier? arg, expr value)"""
    lineno: int
    col_offset: int
    end_lineno: int | None
    end_col_offset: int | None
    if sys.version_info >= (3, 10):
        __match_args__ = ("arg", "value")
    arg: _Identifier | None
    value: expr
    @overload
    def __init__(self, arg: _Identifier | None, value: expr, **kwargs: Unpack[_Attributes]) -> None: ...
    @overload
    def __init__(self, arg: _Identifier | None = None, *, value: expr, **kwargs: Unpack[_Attributes]) -> None: ...

class alias(AST):
    """alias(identifier name, identifier? asname)"""
    lineno: int
    col_offset: int
    end_lineno: int | None
    end_col_offset: int | None
    if sys.version_info >= (3, 10):
        __match_args__ = ("name", "asname")
    name: str
    asname: _Identifier | None
    def __init__(self, name: str, asname: _Identifier | None = None, **kwargs: Unpack[_Attributes]) -> None: ...

class withitem(AST):
    """withitem(expr context_expr, expr? optional_vars)"""
    if sys.version_info >= (3, 10):
        __match_args__ = ("context_expr", "optional_vars")
    context_expr: expr
    optional_vars: expr | None
    def __init__(self, context_expr: expr, optional_vars: expr | None = None) -> None: ...

if sys.version_info >= (3, 10):
    class Match(stmt):
        """Match(expr subject, match_case* cases)"""
        __match_args__ = ("subject", "cases")
        subject: expr
        cases: list[match_case]
        if sys.version_info >= (3, 13):
            def __init__(self, subject: expr, cases: list[match_case] = ..., **kwargs: Unpack[_Attributes]) -> None: ...
        else:
            def __init__(self, subject: expr, cases: list[match_case], **kwargs: Unpack[_Attributes]) -> None: ...

    class pattern(AST):
        """
        pattern = MatchValue(expr value)
        | MatchSingleton(constant value)
        | MatchSequence(pattern* patterns)
        | MatchMapping(expr* keys, pattern* patterns, identifier? rest)
        | MatchClass(expr cls, pattern* patterns, identifier* kwd_attrs, pattern* kwd_patterns)
        | MatchStar(identifier? name)
        | MatchAs(pattern? pattern, identifier? name)
        | MatchOr(pattern* patterns)
        """
        lineno: int
        col_offset: int
        end_lineno: int
        end_col_offset: int
        def __init__(self, **kwargs: Unpack[_Attributes[int]]) -> None: ...

    # Without the alias, Pyright complains variables named pattern are recursively defined
    _Pattern: typing_extensions.TypeAlias = pattern

    class match_case(AST):
        """match_case(pattern pattern, expr? guard, stmt* body)"""
        __match_args__ = ("pattern", "guard", "body")
        pattern: _Pattern
        guard: expr | None
        body: list[stmt]
        if sys.version_info >= (3, 13):
            def __init__(self, pattern: _Pattern, guard: expr | None = None, body: list[stmt] = ...) -> None: ...
        else:
            @overload
            def __init__(self, pattern: _Pattern, guard: expr | None, body: list[stmt]) -> None: ...
            @overload
            def __init__(self, pattern: _Pattern, guard: expr | None = None, *, body: list[stmt]) -> None: ...

    class MatchValue(pattern):
        """MatchValue(expr value)"""
        __match_args__ = ("value",)
        value: expr
        def __init__(self, value: expr, **kwargs: Unpack[_Attributes[int]]) -> None: ...

    class MatchSingleton(pattern):
        """MatchSingleton(constant value)"""
        __match_args__ = ("value",)
        value: Literal[True, False] | None
        def __init__(self, value: Literal[True, False] | None, **kwargs: Unpack[_Attributes[int]]) -> None: ...

    class MatchSequence(pattern):
        """MatchSequence(pattern* patterns)"""
        __match_args__ = ("patterns",)
        patterns: list[pattern]
        if sys.version_info >= (3, 13):
            def __init__(self, patterns: list[pattern] = ..., **kwargs: Unpack[_Attributes[int]]) -> None: ...
        else:
            def __init__(self, patterns: list[pattern], **kwargs: Unpack[_Attributes[int]]) -> None: ...

    class MatchStar(pattern):
        """MatchStar(identifier? name)"""
        __match_args__ = ("name",)
        name: _Identifier | None
        def __init__(self, name: _Identifier | None, **kwargs: Unpack[_Attributes[int]]) -> None: ...

    class MatchMapping(pattern):
        """MatchMapping(expr* keys, pattern* patterns, identifier? rest)"""
        __match_args__ = ("keys", "patterns", "rest")
        keys: list[expr]
        patterns: list[pattern]
        rest: _Identifier | None
        if sys.version_info >= (3, 13):
            def __init__(
                self,
                keys: list[expr] = ...,
                patterns: list[pattern] = ...,
                rest: _Identifier | None = None,
                **kwargs: Unpack[_Attributes[int]],
            ) -> None: ...
        else:
            def __init__(
                self,
                keys: list[expr],
                patterns: list[pattern],
                rest: _Identifier | None = None,
                **kwargs: Unpack[_Attributes[int]],
            ) -> None: ...

    class MatchClass(pattern):
        """MatchClass(expr cls, pattern* patterns, identifier* kwd_attrs, pattern* kwd_patterns)"""
        __match_args__ = ("cls", "patterns", "kwd_attrs", "kwd_patterns")
        cls: expr
        patterns: list[pattern]
        kwd_attrs: list[_Identifier]
        kwd_patterns: list[pattern]
        if sys.version_info >= (3, 13):
            def __init__(
                self,
                cls: expr,
                patterns: list[pattern] = ...,
                kwd_attrs: list[_Identifier] = ...,
                kwd_patterns: list[pattern] = ...,
                **kwargs: Unpack[_Attributes[int]],
            ) -> None: ...
        else:
            def __init__(
                self,
                cls: expr,
                patterns: list[pattern],
                kwd_attrs: list[_Identifier],
                kwd_patterns: list[pattern],
                **kwargs: Unpack[_Attributes[int]],
            ) -> None: ...

    class MatchAs(pattern):
        """MatchAs(pattern? pattern, identifier? name)"""
        __match_args__ = ("pattern", "name")
        pattern: _Pattern | None
        name: _Identifier | None
        def __init__(
            self, pattern: _Pattern | None = None, name: _Identifier | None = None, **kwargs: Unpack[_Attributes[int]]
        ) -> None: ...

    class MatchOr(pattern):
        """MatchOr(pattern* patterns)"""
        __match_args__ = ("patterns",)
        patterns: list[pattern]
        if sys.version_info >= (3, 13):
            def __init__(self, patterns: list[pattern] = ..., **kwargs: Unpack[_Attributes[int]]) -> None: ...
        else:
            def __init__(self, patterns: list[pattern], **kwargs: Unpack[_Attributes[int]]) -> None: ...

if sys.version_info >= (3, 12):
    class type_param(AST):
        """
        type_param = TypeVar(identifier name, expr? bound)
        | ParamSpec(identifier name)
        | TypeVarTuple(identifier name)
        """
        lineno: int
        col_offset: int
        end_lineno: int
        end_col_offset: int
        def __init__(self, **kwargs: Unpack[_Attributes[int]]) -> None: ...

    class TypeVar(type_param):
        """TypeVar(identifier name, expr? bound)"""
        if sys.version_info >= (3, 13):
            __match_args__ = ("name", "bound", "default_value")
        else:
            __match_args__ = ("name", "bound")
        name: _Identifier
        bound: expr | None
        if sys.version_info >= (3, 13):
            default_value: expr | None
            def __init__(
                self,
                name: _Identifier,
                bound: expr | None = None,
                default_value: expr | None = None,
                **kwargs: Unpack[_Attributes[int]],
            ) -> None: ...
        else:
            def __init__(self, name: _Identifier, bound: expr | None = None, **kwargs: Unpack[_Attributes[int]]) -> None: ...

    class ParamSpec(type_param):
        """ParamSpec(identifier name)"""
        if sys.version_info >= (3, 13):
            __match_args__ = ("name", "default_value")
        else:
            __match_args__ = ("name",)
        name: _Identifier
        if sys.version_info >= (3, 13):
            default_value: expr | None
            def __init__(
                self, name: _Identifier, default_value: expr | None = None, **kwargs: Unpack[_Attributes[int]]
            ) -> None: ...
        else:
            def __init__(self, name: _Identifier, **kwargs: Unpack[_Attributes[int]]) -> None: ...

    class TypeVarTuple(type_param):
        """TypeVarTuple(identifier name)"""
        if sys.version_info >= (3, 13):
            __match_args__ = ("name", "default_value")
        else:
            __match_args__ = ("name",)
        name: _Identifier
        if sys.version_info >= (3, 13):
            default_value: expr | None
            def __init__(
                self, name: _Identifier, default_value: expr | None = None, **kwargs: Unpack[_Attributes[int]]
            ) -> None: ...
        else:
            def __init__(self, name: _Identifier, **kwargs: Unpack[_Attributes[int]]) -> None: ...

    class TypeAlias(stmt):
        """TypeAlias(expr name, type_param* type_params, expr value)"""
        __match_args__ = ("name", "type_params", "value")
        name: Name
        type_params: list[type_param]
        value: expr
        if sys.version_info >= (3, 13):
            @overload
            def __init__(
                self, name: Name, type_params: list[type_param], value: expr, **kwargs: Unpack[_Attributes[int]]
            ) -> None: ...
            @overload
            def __init__(
                self, name: Name, type_params: list[type_param] = ..., *, value: expr, **kwargs: Unpack[_Attributes[int]]
            ) -> None: ...
        else:
            def __init__(
                self, name: Name, type_params: list[type_param], value: expr, **kwargs: Unpack[_Attributes[int]]
            ) -> None: ...
