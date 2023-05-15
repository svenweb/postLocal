import unittest

import src.services.ebay.ebay as eb

class TestEbay(unittest.TestCase):
  def test_identifier(self):
    self.assertEqual(eb.test_identifier(), "Ebay")
