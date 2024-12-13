import unittest

def area(a,b):
    try:
        return float(a * b)
    except:
        return "ERROR"

def perimetr(a,b):
    try:
        return 2*float(a+b)
    except:
        return "ERROR"
 
class RectangleTestCase(unittest.TestCase):
    def test_area1(self):
        res = area(10, 15)
        self.assertEqual(res, 150)
    def test_area2(self):
        res = area(10,0)
        self.assertEqual(res, 0)
    def test_area3(self):
        res = area(1,1)
        self.assertEqual(res, 1)
    def test_area4(self):
        res = area(15,5)
        self.assertEqual(res, 75)
    def test_area5(self):
        res = area(28,0.25)
        self.assertEqual(res, 7)
    def test_area6(self):
        res = area(1.5,2)
        self.assertEqual(res, 3)
    def test_area7(self):
        res = area(10,10)
        self.assertEqual(res, 100)
    def test_area8(self):
        res = area(11,12)
        self.assertEqual(res, 132)
    def test_area9(self):
        res = area(0,0)
        self.assertEqual(res, 0)
    def test_areaerror1(self):
        res = area("qwe", 7)
        self.assertEqual(res, "ERROR")
    def test_areaerror2(self):
        res = area("qwe", "123")
        self.assertEqual(res, "ERROR")
    def test_areaerror3(self):
        res = area("qwe", 7)
        self.assertEqual(res, "ERROR")
    def test_areaerror4(self):
        res = area("qwe", "123")
        self.assertEqual(res, "ERROR")
    
    def test_perimetr1(self):
        res = perimetr(10, 15)
        self.assertEqual(res, 50)
    def test_perimetr2(self):
        res = perimetr(10,0)
        self.assertEqual(res, 20)
    def test_perimetr3(self):
        res = perimetr(1,1)
        self.assertEqual(res, 4)
    def test_perimetr4(self):
        res = perimetr(15,5)
        self.assertEqual(res, 40)
    def test_perimetr5(self):
        res = perimetr(28,0.25)
        self.assertEqual(res, 56.5)
    def test_perimetr6(self):
        res = perimetr(1.5,2)
        self.assertEqual(res, 7)
    def test_perimetr7(self):
        res = perimetr(10,10)
        self.assertEqual(res, 40)
    def test_perimetr8(self):
        res = perimetr(11,12)
        self.assertEqual(res, 46)
    def test_perimetr9(self):
        res = perimetr(0,0)
        self.assertEqual(res, 0)
    def test_perimetrerror1(self):
        res = perimetr("qwe", 7)
        self.assertEqual(res, "ERROR")
    def test_perimetrerror2(self):
        res = perimetr("qwe", "123")
        self.assertEqual(res, "ERROR")
    def test_perimetrerror3(self):
        res = perimetr("qwe", 7)
        self.assertEqual(res, "ERROR")
    def test_perimetrerror4(self):
        res = perimetr("qwe", "123")
        self.assertEqual(res, "ERROR")
