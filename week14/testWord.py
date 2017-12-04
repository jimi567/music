import unittest

from word import Word


class TestWord(unittest.TestCase):

    wordList = ['happy', 'word', 'apple', 'current', 'text',
                'guess', 'hangman', 'testcase', 'assignment', 'python']

    def setUp(self):
        self.w1 = Word('wordtest.txt')


    def tearDown(self):
        pass

    def testWord(self):
        self.assertEqual(self.w1.words, self.wordList)
        self.assertEqual(self.w1.count, 10)


    def testRandfromDB(self):
        self.assertIn(self.w1.randFromDB(), self.wordList)

if __name__ == '__main__':
    unittest.main()