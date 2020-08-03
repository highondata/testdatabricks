import unittest
import pkgexample


class TestStringMethods(unittest.TestCase):

    def test_sample(self):
        self.assertEqual(pkgexample.helloWorld(), 1000)

    def test_sample2(self):
        self.assertEqual(pkgexample.helloWorld2(), 499500)

if __name__ == '__main__':
    unittest.main()