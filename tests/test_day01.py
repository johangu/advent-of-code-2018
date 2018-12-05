import unittest

from day01 import part01, part02


class TestDay01(unittest.TestCase):

    def test_part01(self):
        self.assertEqual(3, part01(["+1", "-2", "+3", "+1"]))
        self.assertEqual(3, part01(["+1", "+1", "+1"]))
        self.assertEqual(0, part01(["+1", "+1", "-2"]))
        self.assertEqual(-6, part01(["-1", "-2", "-3"]))

    def test_part02(self):
        self.assertEqual(0, part02(["+1", "-1"]))
        self.assertEqual(2, part02(["+1", "-2", "+3", "+1"]))
        self.assertEqual(10, part02(["+3", "+3", "+4", "-2", "-4"]))
        self.assertEqual(5, part02(["-6", "+3", "+8", "+5", "-6"]))
        self.assertEqual(14, part02(["+7", "+7", "-2", "-7", "-4"]))


if __name__ == '__main__':
    unittest.main()
