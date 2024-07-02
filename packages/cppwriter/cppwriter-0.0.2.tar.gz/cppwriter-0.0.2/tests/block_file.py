from test_config import INDENT_CHAR
from test_utils import strip_nl

from cppwriter import FileBlock


def test_include():
    """Test file block generation"""
    file = FileBlock(INDENT_CHAR)
    file.include("stdio.h", is_global=True)
    file.include("handler.h")
    assert str(file) == strip_nl("""
#include <stdio.h>
#include "handler.h"
""")

def test_pragma():
    """Test file block generation"""
    file = FileBlock(INDENT_CHAR)
    file.pragma("once")
    file.pragma("region Region_1")
    file.comment("Region comment")
    file.pragma("endregion Region_1")
    assert str(file) == strip_nl("""
#pragma once
#pragma region Region_1
// Region comment
#pragma endregion Region_1
""")

def test_function():
    """Test function block generation"""
    file = FileBlock(INDENT_CHAR)
    file.include("stdio.h", is_global=True)
    func = file.function("int main()")
    func.line("return 0")
    assert str(file) == strip_nl("""
#include <stdio.h>
int main() {
    return 0;
}
""")

def test_enum():
    """Test enum block generation"""
    file = FileBlock(INDENT_CHAR)
    enum = file.enum("Color")
    enum.item("Red")
    assert str(file) == strip_nl("""
enum Color {
    Red,
};
""")
