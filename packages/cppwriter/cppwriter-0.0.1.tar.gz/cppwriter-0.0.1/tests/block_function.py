from test_config import INDENT_CHAR
from test_utils import strip_nl

from cppwriter import FunctionBlock


def test_basic_function_block():
    """Test enum generation"""
    func = FunctionBlock("int main()", INDENT_CHAR)
    func.line("return 0")

    assert str(func) == strip_nl("""
int main() {
    return 0;
}
""")

def test_if_statement():
    """Test if statement generation"""
    func = FunctionBlock("int main()", INDENT_CHAR)
    if_block = func.if_statement("a == 0")
    if_block.line("return 0")

    assert str(func) == strip_nl("""
int main() {
    if (a == 0) {
        return 0;
    }
}
""")

def test_while_statement():
    """Test while statement generation"""
    func = FunctionBlock("int main()", INDENT_CHAR)
    while_block = func.while_statement("a == 0")
    while_block.line("return 0")

    assert str(func) == strip_nl("""
int main() {
    while (a == 0) {
        return 0;
    }
}
""")

def test_nesting():
    """Test if statement generation"""
    func = FunctionBlock("int main()", INDENT_CHAR)
    if_block = func.if_statement("a == 0")
    nested_block = if_block.if_statement("b == 0")
    while_block = nested_block.while_statement("b == 0")
    while_block.line("return 1")
    func.line("return 0")

    assert str(func) == strip_nl("""
int main() {
    if (a == 0) {
        if (b == 0) {
            while (b == 0) {
                return 1;
            }
        }
    }
    return 0;
}
""")

def test_switch_statement():
    """Test switch statement generation"""
    func = FunctionBlock("int main()", INDENT_CHAR)
    switch_block = func.switch_statement("a")
    switch_block.case_statement("0").line("return 0")
    switch_block.case_statement("1").line("return 1")
    switch_block.default_statement().line("return 2")

    assert str(func) == strip_nl("""
int main() {
    switch (a) {
        case 0:
            return 0;
        case 1:
            return 1;
        default:
            return 2;
    }
}
""")
    
def test_for_statement():
    """Test for statement generation"""
    func = FunctionBlock("int main()", INDENT_CHAR)
    for_block = func.for_statement("int i = 0; i < 10; i++")
    for_block.line("i++")
    func.line("return 0")

    assert str(func) == strip_nl("""
int main() {
    for (int i = 0; i < 10; i++) {
        i++;
    }
    return 0;
}
""")
