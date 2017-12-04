import unittest

from guess import Guess

class TestGuess(unittest.TestCase):

    def setUp(self):
        self.g1 = Guess('default')

    def tearDown(self):
        pass

    def testDisplayCurrent(self):
        self.assertEqual(self.g1.displayCurrent(), '_ e _ _ _ _ _ ')
        self.g1.guess('a')
        self.assertEqual(self.g1.displayCurrent(), '_ e _ a _ _ _ ')
        self.g1.guess('t')
        self.assertEqual(self.g1.displayCurrent(), '_ e _ a _ _ t ')
        self.g1.guess('u')
        self.assertEqual(self.g1.displayCurrent(), '_ e _ a u _ t ')
        #틀린 글자
        self.g1.guess('c')
        self.assertEqual(self.g1.displayCurrent(), '_ e _ a u _ t ')
        #두글자 이상
        self.g1.guess('ab')
        self.assertEqual(self.g1.displayCurrent(), '_ e _ a u _ t ')
        #중복된 글자
        self.g1.guess('a')
        self.assertEqual(self.g1.displayCurrent(), '_ e _ a u _ t ')
        #한글
        self.g1.guess('ㄹ')
        self.assertEqual(self.g1.displayCurrent(), '_ e _ a u _ t ')
        #숫자
        self.g1.guess('3')
        self.assertEqual(self.g1.displayCurrent(), '_ e _ a u _ t ')
        #기호
        self.g1.guess('!')
        self.assertEqual(self.g1.displayCurrent(), '_ e _ a u _ t ')



    def testDisplayGuessed(self):
        self.assertEqual(self.g1.displayGuessed(), ' e n ')
        self.g1.guess('a')
        self.assertEqual(self.g1.displayGuessed(), ' a e n ')
        self.g1.guess('t')
        self.assertEqual(self.g1.displayGuessed(), ' a e n t ')
        self.g1.guess('u')
        self.assertEqual(self.g1.displayGuessed(), ' a e n t u ')
        #틀린 글자
        self.g1.guess('c')
        self.assertEqual(self.g1.displayGuessed(), ' a c e n t u ')
        #중복된 글자
        self.g1.guess('a')
        self.assertEqual(self.g1.displayGuessed(), ' a c e n t u ')
        #한글
        self.g1.guess('ㄹ')
        self.assertEqual(self.g1.displayGuessed(), ' a c e n t u ㄹ ')
        #숫자
        self.g1.guess('3')
        self.assertEqual(self.g1.displayGuessed(), ' 3 a c e n t u ㄹ ')
        #기호
        self.g1.guess('!')
        self.assertEqual(self.g1.displayGuessed(), ' ! 3 a c e n t u ㄹ ')


    def testGuess(self):
        #secretword에 character가 없으면 False, 있으면 True return.
        self.assertFalse(self.g1.guess('c'))
        self.assertTrue(self.g1.guess('a'))

        #currentStatus 상태 확인
        self.assertEqual(self.g1.currentStatus, '_e_a___')
        self.g1.guess('t')
        self.assertEqual(self.g1.currentStatus, '_e_a__t')
        self.g1.guess('u')
        self.assertEqual(self.g1.currentStatus, '_e_au_t')
        self.g1.guess('ab')
        self.assertEqual(self.g1.currentStatus, '_e_au_t')
        self.g1.guess('a')
        self.assertEqual(self.g1.currentStatus, '_e_au_t')
        self.g1.guess('ㄹ')
        self.assertEqual(self.g1.currentStatus, '_e_au_t')
        self.g1.guess('3')
        self.assertEqual(self.g1.currentStatus, '_e_au_t')
        self.g1.guess('!')
        self.assertEqual(self.g1.currentStatus, '_e_au_t')

    def testFinished(self):
        #다 맞추기 전과 맞춘 경우 return값 확인.
        self.assertFalse(self.g1.finished())
        self.g1.guess('a')
        self.assertFalse(self.g1.finished())
        self.g1.guess('d')
        self.assertFalse(self.g1.finished())
        self.g1.guess('f')
        self.assertFalse(self.g1.finished())
        self.g1.guess('u')
        self.assertFalse(self.g1.finished())
        self.g1.guess('l')
        self.assertFalse(self.g1.finished())
        self.g1.guess('t')
        #self.currentStatus == self.secretWord
        self.assertTrue(self.g1.finished())


if __name__ == '__main__':
    unittest.main()

#두글자 이상, 틀린글자, 중복된 글자 , 한글 ,숫자 기호, 등