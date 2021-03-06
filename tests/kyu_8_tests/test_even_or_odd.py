import unittest

from katas.kyu_8.even_or_odd import even_or_odd


class EvenOrOddTestCase(unittest.TestCase):
    def test_equals(self):
        self.assertEqual(even_or_odd(2), 'Even')

    def test_equals_2(self):
        self.assertEqual(even_or_odd(11), 'Odd')
