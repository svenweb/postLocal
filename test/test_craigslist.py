import sys
sys.path.append("./")

import unittest

from src.services.craigslist import craigslist as cl

class TestCraigslist(unittest.TestCase):
  def test_identifier(self):
    self.assertEqual(cl.test_identifier(), "Craigslist")
