import unittest

def area(a,b):
    try:
        return float(a * b)
    except:
        return "ERROR"
 
class RectangleTestCase(unittest.TestCase):
    def test_0(self):
        res = area(10, 15)
        self.assertEqual(res, 150)
    def test_1(self):
        res = area(10,0)
        self.assertEqual(res, 0)
    def test_2(self):
        res = area("qwe", 7)
        self.assertEqual(res, "ERROR")
    def test_3(self):
        res = area("qwe", "123")
        self.assertEqual(res, "ERROR")
    
