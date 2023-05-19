import sys
sys.path.append("./")

import unittest

from src.services.ebay import ebay as eb

class TestEbay(unittest.TestCase):
  def test_identifier(self):
    self.assertEqual(eb.test_identifier(), "Ebay")
