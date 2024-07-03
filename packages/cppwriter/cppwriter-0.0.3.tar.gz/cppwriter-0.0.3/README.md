# C++ writer [![Quality assurance](https://github.com/mishamyrt/cppwriter/actions/workflows/qa.yaml/badge.svg)](https://github.com/mishamyrt/cppwriter/actions/workflows/qa.yaml) [![PyPI version](https://badge.fury.io/py/cppwriter.svg)](https://badge.fury.io/py/cppwriter)

The library provides an iterative interface for generating C/C++ code from Python.

## Installation

```sh
pip install cppwriter
```

## Usage

```python
from cppwriter import FileBlock

file = FileBlock(indent_char="  ")
file.include("stdio.h", is_global=True)
file.line()
main = file.function("main", "int")
main.if_statement("PI > 4").line("return 1")
main.line("return 0")
print(str(file))
```

This will generate the following code:

```c
#include <stdio.h>

int main() {
  if (PI > 4) {
    return 1;
  }
  return 0;
}
```

## Relationship to cwriter

When I started making this library I didn't know about the existence of cwriter. I came across it while searching for a package name, but decided to give up and still finish my version.  