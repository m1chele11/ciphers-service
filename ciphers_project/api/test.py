from django.test import TestCase
from .ciphers import caeser_encode



class CiphersTest(TestCase):
    def test_caesar_encoding_1(self):
        plain_text = 'hello'
        shift = 1 
        expected = "ifmmp"
        output = caeser_encode(plain_text, shift)
        self.assertEqual(expected, output)


    def test_caesar_encoding_1(self):
        plain_text = 'winter'
        shift = 3 
        expected = "zlqwhu"
        output = caeser_encode(plain_text, shift)
        self.assertEqual(expected, output)