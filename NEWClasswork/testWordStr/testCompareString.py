import unittest
from NEWClasswork import CompareTwoString

class TestStringWord(unittest.TestCase):
    def test_that_i_have_Two_String_Word(self):
        actual = 'text' and 'ending'
        expected = 'true'
        self.assertTrue(actual, expected)

        def test_that_the_word_is_true_or_false(self):
            actual = 'text' == 'ending'
            expected = 'true' or 'false'
            self.assertEqual(actual, expected)


if __name__ == '__main__':
    unittest.main()
