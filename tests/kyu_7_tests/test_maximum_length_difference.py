import unittest

from kyu_7.maximum_length_difference import mxdiflg


class MaximumLengthDifferenceTestCase(unittest.TestCase):
    def test_equals(self):
        self.assertEqual(mxdiflg([
            'hoqq', 'bbllkw', 'oox', 'ejjuyyy', 'plmiis', 'xxxzgpsssa',
            'xxwwkktt', 'znnnnfqknaz', 'qqquuhii', 'dvvvwz'
        ], ['cccooommaaqqoxii', 'gggqaffhhh', 'tttoowwwmmww']), 13)


if __name__ == '__main__':
    unittest.main()
