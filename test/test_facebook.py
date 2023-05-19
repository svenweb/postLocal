import sys
sys.path.append("./")

import unittest

from src.services.facebook import facebook as fb

class TestFacebook(unittest.TestCase):
  def test_identifier(self):
    self.assertEqual(fb.test_identifier(), "Facebook")
