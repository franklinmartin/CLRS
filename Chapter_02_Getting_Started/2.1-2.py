import random
import unittest

""" 2.1-2
Consider the procedure SUM-ARRAY on the facing page. It computes
the sum of the n numbers in array A[1 : n]. State a loop invariant for this
procedure, and use its initialization, maintenance, and termination
properties to show that the SUM-ARRAY procedure returns the sum of
the numbers in A[1 : n]. """

def insertion_sort(a):
    for i in range(2, len(a)):
        key = a[i]
        j = i - 1
        while j > 0 and a[j] > key:
            a[j + 1] = a[j]
            j -= 1
        a[j + 1] = key

class InsertionSortTestCase(unittest.TestCase):
    def random_array(self):
        return [random.randint(0, 100) for _ in range(random.randint(1, 100))]

    def test_random(self):
        for _ in range(10000):
            arr = self.random_array()
            sorted_arr = sorted(arr)
            sorted_arr.reverse()
            insertion_sort(arr)
            self.assertEqual(arr, sorted_arr)


if __name__ == '__main__':
    unittest.main()
