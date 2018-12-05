import unittest

from day02 import part01, part02


class TestDay02(unittest.TestCase):

    def test_part01(self):
        self.assertEqual(12, part01(['aabcdd', 'ababab', 'abcdee',
                                    'abcdef', 'bababc', 'abbcde', 'abcccd']))

    # def test_part02(self):
    #     self.assertEqual('fgij', part02(['abcde', 'fghij', 'klmno',
    #                                     'pqrst', 'fguij', 'axcye', 'wvxyz']))


if __name__ == '__main__':
    unittest.main()
