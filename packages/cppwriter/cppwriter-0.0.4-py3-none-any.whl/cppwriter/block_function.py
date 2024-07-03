"""C++ writer function block"""
from .block import Block


def format_function_header(name: str, return_type: str, args: list = None) -> str:
    """Returns function name"""
    header = f"{return_type} {name}("
    if args is not None:
        header += ", ".join(args)
    header += ")"
    return header

class FunctionBlock(Block):
    """C/C++ function body block"""
    _curly_wrapped: bool

    def __init__(self, header: str, indent_char: str, indent="", curly_wrapped=True) -> None:
        super().__init__(indent_char, indent + indent_char)
        self._curly_wrapped = curly_wrapped
        if curly_wrapped:
            header = f"{header} {{"
        self.line(header, semi=False, indent=indent)

    def if_statement(self, condition: str) -> "FunctionBlock":
        """Adds an if statement block"""
        block = FunctionBlock(f"if ({condition})", self._indent_char, self._current_indent)
        self._body.append(block)
        return block

    def switch_statement(self, condition: str) -> "FunctionBlock":
        """Adds a switch statement block"""
        block = FunctionBlock(
            f"switch ({condition})",
            self._indent_char, self._current_indent)
        self._body.append(block)
        return block

    def case_statement(self, condition: str) -> "FunctionBlock":
        """Adds a case statement block"""
        block = FunctionBlock(
            f"case {condition}:",
            self._indent_char, self._current_indent,
            curly_wrapped=False)
        self._body.append(block)
        return block

    def default_statement(self) -> "FunctionBlock":
        """Adds a default statement block"""
        block = FunctionBlock(
            "default:",
            self._indent_char, self._current_indent,
            curly_wrapped=False)
        self._body.append(block)
        return block

    def while_statement(self, condition: str) -> "FunctionBlock":
        """Adds a while statement block"""
        block = FunctionBlock(f"while ({condition})", self._indent_char, self._current_indent)
        self._body.append(block)
        return block

    def for_statement(self, condition: str) -> "FunctionBlock":
        """Adds a for statement block"""
        block = FunctionBlock(f"for ({condition})", self._indent_char, self._current_indent)
        self._body.append(block)
        return block

    def __str__(self) -> str:
        """Returns block content"""

        if self._curly_wrapped:
            self._body.append(f"{self._current_indent[:-len(self._indent_char)]}}}\n")
        content = self._join_body()
        return content
