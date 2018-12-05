import unittest

from day03 import part01, part02


class TestDay03(unittest.TestCase):

    def test_part01(self):
        data = ["#1 @ 1,3: 4x4", "#2 @ 3,1: 4x4", "#3 @ 5,5: 2x2"]
        self.assertEqual(4, part01(data))

    def test_part02(self):
        data = ["#1 @ 1,3: 4x4", "#2 @ 3,1: 4x4", "#3 @ 5,5: 2x2"]
        self.assertEqual("#3", part02(data))


if __name__ == "__main__":
    unittest.main()
