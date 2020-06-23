import unittest
from score import Score

class TestCar(unittest.TestCase):

    def setUp(self):
        self.my_score = Score("1111,홍길동,90,70,80")

    def tearDown(self):
        del self.my_score

    def test_constructor(self):
        self.assertIsNotNone(self.my_score)


    def test_sid_1(self):
        self.assertEqual("1111", self.my_score.sid)

    def test_name(self):
        self.assertEqual("홍길동", self.my_score.name)

    def test_kor(self):
        self.assertEqual(90, self.my_score.kor)

    def test_eng(self):
        self.assertEqual(70, self.my_score.eng)

    def test_math(self):
        self.assertEqual(80, self.my_score.math)

    def test_total(self):
        self.assertEqual(240, self.my_score.total)

    def test_avg(self):
        self.assertEqual(80, self.my_score.avg)
        

if __name__ == "__main__":
    pass
