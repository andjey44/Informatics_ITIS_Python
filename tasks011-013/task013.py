import unittest
import Task011
import Task012
class testing(unittest.TestCase):
    def setUp(self) -> None:
        self.Task011 = Task011.Homework()
        self.Task012 = Task012.Homework()

    def test1(self):
        self.assertEqual(self.Task011.first_metod(),10)

    def test4(self):
        with self.assertRaises(KeyError):
            Task012.calculator(opr1='+', opr2=1, opr3='*', opr4='+')
if __name__ == '__main__':
    unittest.main()
