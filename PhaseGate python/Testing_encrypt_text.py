import encrypt_text
from unittest import TestCase

class TestEncryption(unittest.TestCase):
	
	def test_encrypt_function_exits(self):
		encrypt_test_get_encryption

	def test_encrypt_text_with_simple_ROT13_cipher_using_strings(self):
		actual = encrypt_text(" ")
		expected = " "
		self.assertEqual(actual,expected)
	def test_each_letter_is_shifted_by_thirteeth_positions_in_the_alphabet_wrapping_around_it(self):
		actual = get_text_encryption("Animation")
		expected = "nzvynfvaz"
		self.assertEqual(actual, encrypt_test_get_encryption)
		self.assertEqual(expected, encrypted_test, "nzvynfvaz")

		
		