"""C++ writer file block"""
from .block import Block
from .block_enum import EnumBlock
from .block_function import FunctionBlock


class FileBlock(Block):
    """C/C++ file block"""
    def __init__(self, indent_char: str) -> None:
        super().__init__(indent_char)

    def include(self, path: str, is_global=False) -> None:
        """Adds include statement to file"""
        if is_global:
            self.line(f"#include <{path}>", semi=False)
        else:
            self.line(f'#include "{path}"', semi=False)

    def pragma(self, value: str) -> None:
        """Adds pragma statement to file"""
        self.line(f"#pragma {value}", semi=False)

    def function(self, header: str) -> FunctionBlock:
        """Creates function block"""
        block = FunctionBlock(header, self._indent_char)
        self._body.append(block)
        return block

    def enum(self, name: str, enum_type: str = None) -> EnumBlock:
        """Creates enum block"""
        block = EnumBlock(name, self._indent_char, enum_type)
        self._body.append(block)
        return block
