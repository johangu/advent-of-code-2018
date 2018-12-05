import unittest

from day05 import part01, part02


class TestDay05(unittest.TestCase):

    def test_part01(self):
        self.assertEqual(10, part01('dabAcCaCBAcCcaDA'))

    def test_part02(self):
        self.assertEqual(4, part02('dabAcCaCBAcCcaDA'))
