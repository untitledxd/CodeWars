import unittest

from katas.kyu_5.caesar_cipher_helper import CaesarCipher


class CaesarCipherTestCase(unittest.TestCase):
    def setUp(self):
        self.caesar = CaesarCipher(5)

    def test_equals(self):
        self.assertEqual(self.caesar.encode('Codewars'), 'HTIJBFWX')

    def test_equals_2(self):
        self.assertEqual(self.caesar.decode('BFKKQJX'), 'WAFFLES')
