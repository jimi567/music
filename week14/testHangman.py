import unittest

from hangman import Hangman

class TestHangman(unittest.TestCase):

    def setUp(self):
        self.h1 = Hangman()


    def tearDown(self):
        pass


    def testHangman(self):
        #처음 상태의 목숨 개수
        self.assertEqual(self.h1.remainingLives,6)
        #점점 줄어드는 목숨
        self.h1.decreaseLife()
        self.assertEqual(self.h1.remainingLives,5)
        self.h1.decreaseLife()
        self.assertEqual(self.h1.remainingLives,4)
        self.h1.decreaseLife()
        self.assertEqual(self.h1.remainingLives,3)
        self.h1.decreaseLife()
        self.assertEqual(self.h1.remainingLives,2)
        self.h1.decreaseLife()
        self.assertEqual(self.h1.remainingLives,1)
        self.h1.decreaseLife()
        self.assertEqual(self.h1.remainingLives,0)

    def testCurrentShape(self):
        self.assertEqual(self.h1.currentShape(),self.h1.text[self.h1.remainingLives])
        self.h1.decreaseLife()
        self.assertEqual(self.h1.currentShape(),self.h1.text[5])
        self.h1.decreaseLife()
        self.assertEqual(self.h1.currentShape(),self.h1.text[4])
        self.h1.decreaseLife()
        self.assertEqual(self.h1.currentShape(),self.h1.text[3])
        self.h1.decreaseLife()
        self.assertEqual(self.h1.currentShape(),self.h1.text[2])
        self.h1.decreaseLife()
        self.assertEqual(self.h1.currentShape(),self.h1.text[1])
        self.h1.decreaseLife()
        self.assertEqual(self.h1.currentShape(),self.h1.text[0])


if __name__ == '__main__':
    unittest.main()