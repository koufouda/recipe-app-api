"""
Sample Tests
"""

from django.test import SimpleTestCase

from app import calc

class CalcTests(SimpleTestCase):
    """Test the calc module """

    def test_add_numbers(self):
        """Test Ading numbers"""
        res = calc.add(5,13)
        self.assertEqual(res,18)
        
        res = calc.add(1,13)
        self.assertEqual(res,14)

        res = calc.add(-5,-13)
        self.assertEqual(res,-18)


    def test_subtract_numbers(self):
        """Test test_subtract_numbers numbers"""
        res = calc.subtract(5,13)
        self.assertEqual(res,-8)



