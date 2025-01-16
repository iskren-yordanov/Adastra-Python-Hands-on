"""With a good naming convention you can run all unit tests (e.g. in a folder named tests) from the console like this: python -m unittest discover tests
You can generate test coverage information using the coverage module: coverage run -m unittest discover tests. Then usecoverage reportto see the results.
There are various choices of testing frameworks for python, e.g. Robot, PyTest, Unittest, DocTest,Nose2, Testify. Some of them are just extensions of unittest, others are stand-alone frameworks.
"""

from unittest import TestCase
from Book_unit170.calculator import Calculation

class CalculationTestCase(TestCase):
    
    def setUp(self) -> None:
        "Set up an instance before each test"
        self.calc = Calculation()

    def tearDown(self):
        "Any cleanup"
        return super().tearDown()

    def test_add(self): 
        #calc = Calculation() 
        result = self.calc.add(3, 8) 
        assert result == 11

    def test_subtract(self): 
        #calc = Calculation() 
        result = self.calc.subtract(7, 3) 
        assert result == 4
        
    def test_multiply(self): 
        #calc = Calculation() 
        result = self.calc.multiply(12, 5) 
        self.assertEqual(result,60,"testing multiply option")

    def test_divide(self): 
        #calc = Calculation() 
        result = self.calc.divide(12, 4) 
        assert result == 3

    def test_divide_by_zero(self):
        with self.assertRaises(ValueError):
            self.calc.divide(1,0)
