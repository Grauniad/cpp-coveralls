#!/bin/bash

rm -rf build

python3 ./setup.py build

mkdir -p target/lib/python3.6/site-packages/
export PYTHONPATH="$PWD/target/lib/python3.6/site-packages/"

python3 ./setup.py install --prefix=target

export PATH="$PWD/test-utils/:$PWD/target/bin/:$PATH"

which cpp-coveralls || exit 1
which check_output.py || exit 1


./test.bash -e || exit 1
