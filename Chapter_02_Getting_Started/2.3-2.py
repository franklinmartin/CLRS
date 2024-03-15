import unittest
import random

def merge_sort_sub (a, l, r):
    if l >= r:
        return
    mid = (l + r) // 2
    merge_sort_sub(a, l, mid)
    merge_sort_sub(a, mid + 1, r)
    a_l, a_r = [], []
    for i in range(l, mid + 1):
        a_l.append(a[i])
    for j in range(mid + 1, rt + 1):
        a_r.append(a[j])
    i, j = 0, 0
    for k in range(l, r + 1):
        



class MergeSortTestCase(unittest.TestCase):
    def random_array(self):
        return [random.randint(0, 100) for _ in range(random.randint(1, 100))]

    def test_random(self):
        for _ in range(10000):
            arr = self.random_array()
            sorted_arr = sorted(arr)
            merge_sort(arr)
            self.assertEqual(arr, sorted_arr)


if __name__ == '__main__':
    unittest.main()
