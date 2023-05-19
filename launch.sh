#!/bin/bash

# determine whether to run the actual application or integration tests
if [ "$1" == "reset" ]
then
  echo "Reset -> reinstalling requirements..."
  pip3 install -r requirements.txt

  echo "Reset -> reinstalling rust modules..."
  cd utility

  cargo build --release
  cp target/release/libutility.so ../lib
  mv ../lib/libutility.so ../lib/utility.so

  cd ..
elif [ "$1" == "run" ]
then
  python3 src/main.py
else
  # -v must be at end -> verbose flag for unittest
  python3 test/test_main.py -v
fi