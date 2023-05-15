import unittest

import src.services.kijiji.kijiji as kj

class TestKijiji(unittest.TestCase):
  def test_identifier(self):
    self.assertEqual(kj.test_identifier(), "Kijiji")
