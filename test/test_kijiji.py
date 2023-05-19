import sys
sys.path.append("./")

import unittest

from src.services.kijiji import kijiji as kj

class TestKijiji(unittest.TestCase):
  def test_identifier(self):
    self.assertEqual(kj.test_identifier(), "Kijiji")
