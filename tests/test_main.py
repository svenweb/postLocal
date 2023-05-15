import unittest

# import all symbols to run the unit tests.
# polluting global namespace is generally a bad idea, 
# but this file is just for running the integration tests.
from test_craigslist import *
from test_facebook import *
from test_kijiji import *
from test_ebay import *

# some example test predicates:
# self.assertTrue
# self.assertFalse
# self.assertEqual
# self.asserRaises
def main():
  unittest.main()

if __name__ == "__main__":
  main()