"""C++ Writer test utils"""

def strip_nl(x: str) -> str:
    """Strips newline from the beginning of the string"""
    if x[0] == "\n":
        x = x[1:]
    return x
