import unittest

import src.services.facebook.facebook as fb

class TestFacebook(unittest.TestCase):
  def test_identifier(self):
    self.assertEqual(fb.test_identifier(), "Facebook")
