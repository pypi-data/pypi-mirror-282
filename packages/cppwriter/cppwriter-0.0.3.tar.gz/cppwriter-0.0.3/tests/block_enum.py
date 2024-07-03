"""Enum block tests"""
from test_config import INDENT_CHAR
from test_utils import strip_nl

from cppwriter.block_enum import EnumBlock, format_enum_header


def test_format_enum_header():
    """Test enum name formatting"""
    assert format_enum_header("foo") == "enum foo"
    assert format_enum_header("foo", "int") == "enum foo : int"


def test_typed():
    """Test enum generation"""
    colors = EnumBlock("Color", INDENT_CHAR, "uint32_t")
    colors.item("Red", "0x00FF0000")
    colors.item("Green", "0x0000FF00")
    colors.item("Blue", "0x000000FF")

    assert str(colors) == strip_nl("""
enum Color : uint32_t {
    Red = 0x00FF0000,
    Green = 0x0000FF00,
    Blue = 0x000000FF,
};
""")

def test_untyped():
    """Test enum generation"""
    colors = EnumBlock("Color", INDENT_CHAR)
    colors.item("Red")
    colors.item("Green")
    colors.item("Blue")

    assert str(colors) == strip_nl("""
enum Color {
    Red,
    Green,
    Blue,
};
""")

def test_from_dict():
    """Test enum generation"""
    colors = EnumBlock.from_dict("Color", {
        "Red": "0x00FF0000",
        "Green": "0x0000FF00",
        "Blue": "0x000000FF",
    }, INDENT_CHAR, "uint32_t")

    assert str(colors) == strip_nl("""
enum Color : uint32_t {
    Red = 0x00FF0000,
    Green = 0x0000FF00,
    Blue = 0x000000FF,
};
""")

def test_from_list():
    """Test enum generation"""
    colors = EnumBlock.from_list("Color", [
        "Red",
        "Green",
        "Blue",
    ], INDENT_CHAR)

    assert str(colors) == strip_nl("""
enum Color {
    Red,
    Green,
    Blue,
};
""")
