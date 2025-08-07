import unittest

from NEWClasswork import takesWord


class MyTestCase(unittest.TestCase):
    def test_thatTheWordFunctionExist(self):
        takesWord.getWordFunction()

    def test_thatTheWordFunctionCanDivideTheWordEqual(self):
        actual = takesWord.getWordFunction()
        expected = "helceloo"
        self.assertEqual(actual, expected)




if __name__ == '__main__':
    unittest.main()
