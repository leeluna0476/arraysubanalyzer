#!/bin/bash

clang -Xclang -ast-dump=json -fsyntax-only $1 | python3 srcs/test.py
