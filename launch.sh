#!/bin/bash

# determine whether to run the actual application or integration tests
if [ "$1" == "reset" ]
then
  echo "Reset -> reinstalling requirements..."
  pip install -r requirements.txt
elif [ "$1" == "run" ]
then
  python3 src/main.py
else
  # -v must be at end -> verbose flag for unittest
  python3 tests/test_main.py -v
fi
