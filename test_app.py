import unittest
from app import app

class CalculatorTestCase(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_addition(self):
        response = self.app.post('/calculate', data=dict(num1='10', num2='5', operation='add'))
        self.assertIn(b'Result: 15.0', response.data)

    def test_subtraction(self):
        response = self.app.post('/calculate', data=dict(num1='10', num2='5', operation='subtract'))
        self.assertIn(b'Result: 5.0', response.data)

    def test_multiplication(self):
        response = self.app.post('/calculate', data=dict(num1='10', num2='5', operation='multiply'))
        self.assertIn(b'Result: 50.0', response.data)

    def test_division(self):
        response = self.app.post('/calculate', data=dict(num1='10', num2='5', operation='divide'))
        self.assertIn(b'Result: 2.0', response.data)

if __name__ == '__main__':
    unittest.main()
