import unittest

import src.services.craigslist.craigslist as cl

class TestCraigslist(unittest.TestCase):
  def test_identifier(self):
    self.assertEqual(cl.test_identifier(), "Craigslist")
