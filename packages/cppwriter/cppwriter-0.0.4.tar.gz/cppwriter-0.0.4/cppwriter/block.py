"""C/C++ generator block"""
from __future__ import annotations


class Block:
    """Block of C/C++ code"""

    _body: list[str | Block]
    _indent_char: str
    _current_indent: str

    def __init__(self, indent_char: str, current_indent="") -> None:
        self._body = []
        self._indent_char = indent_char
        self._current_indent = current_indent

    def comment(self, text: str) -> None:
        """Adds a comment to the block body"""
        self._print(f"// {text}\n")

    def line(self, code="", semi=True, indent: str = None, amend=False) -> None:
        """Adds a line of code to the block body"""
        if len(code) > 0:
            if semi:
                code += ";"
            self._print(f"{code}\n", indent, amend)
        else:
            self._print("\n", indent, amend)

    def block(self) -> Block:
        """Adds a nested block of code to the block body"""
        block = Block(self._indent_char, self._current_indent)
        self._body.append(block)
        return block

    def add_block(self, block: Block) -> None:
        """Adds a block to the block body"""
        self._body.append(block)

    def __str__(self) -> str:
        """Returns block content"""
        return self._join_body()

    def _print(self, x: str, indent: str = None, amend=False) -> None:
        if indent is None:
            indent = self._current_indent
        if amend:
            self._body[-1] = f"{indent}{x}"
        else:
            self._body.append(f"{indent}{x}")

    def _join_body(self) -> str:
        content = ""
        for item in self._body:
            content += str(item)
        return content
