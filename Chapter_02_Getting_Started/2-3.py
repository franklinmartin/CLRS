import unittest

def horner_evaluate_polynomial(a, x):
    p = 0
    #rnge(start, stop, step)
    for i in range(len(a) - 1, -1, -1):
        p = a[i] + x * p
    return p

def polynomial_evaluation(a, x):
    p = 0
    for i in range(len(a)):
        p += a[i] * x ** i
    return p

class HornerTestCase(unittest.TestCase):
    def test_empty(self):
        self.assertEqual(horner_evaluate_polynomial([], 1), 0)
        self.assertEqual(polynomial_evaluation([], 1), 0)

    def test_const(self):
        self.assertEqual(horner_evaluate_polynomial([3], 2), 3)
        self.assertEqual(polynomial_evaluation([3], 2), 3)

    def test_cubic(self):
        self.assertEqual(horner_evaluate_polynomial([1, 2, 3], 4), 57)
        self.assertEqual(polynomial_evaluation([1, 2, 3], 4), 57)

    def test_negative(self):
        self.assertEqual(horner_evaluate_polynomial([-1, 2, -3], -4), -57)
        self.assertEqual(polynomial_evaluation([-1, 2, -3], -4), -57)

if __name__ == '__main__':
    unittest.main()