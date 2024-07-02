"""C++ writer enum block"""
from .block import Block


def format_enum_header(name: str, enum_type: str = None) -> str:
    """Returns enum header"""
    header = f"enum {name}"
    if enum_type:
        header += f" : {enum_type}"
    return header

class EnumBlock(Block):
    """Code block for C/C++ enum"""
    _header: str

    def __init__(self, name: str, indent_char: str, enum_type: str = None) -> None:
        self._header = format_enum_header(name, enum_type)
        super().__init__(indent_char)

    def item(self, name: str, value: str = None) -> None:
        """Adds an enumerator item to the block body"""
        enumerator = f"{self._indent_char}{name}"
        if value is not None:
            enumerator += f" = {value}"
        enumerator += ","
        self.line(enumerator, semi=False)

    def __str__(self) -> str:
        """Returns enum content"""
        return self._header + " {\n" + self._join_body() + "};\n"

    @staticmethod
    def from_dict(name: str, x: dict, indent_char: str, enum_type: str = None) -> "EnumBlock":
        """Returns enum block from a dictionary"""
        enum = EnumBlock(name, indent_char, enum_type)
        for key, value in x.items():
            enum.item(key, value)
        return enum

    @staticmethod
    def from_list(name: str, x: list, indent_char: str, enum_type: str = None) -> "EnumBlock":
        """Returns enum block from a list"""
        enum = EnumBlock(name, indent_char, enum_type)
        for item in x:
            enum.item(item)
        return enum
