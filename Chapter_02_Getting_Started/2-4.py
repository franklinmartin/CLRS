import random
import unittest

#merge sort modifications
#determine # of inversions in any permutation of n elements
#def count_inversion_sub(a):

#Hint: Modify merge sort.
#Big Theta nlgn


def count_inversion_ms(a, l, r):
    if l >= r:
        return 0
    mid = (l + r) // 2
    count = count_inversion_ms(a, l, mid) + count_inversion_ms(a, mid + 1, r)
    a_l =[a[i] for i in range(l, mid + 1)]
    a_l.append(1e100)
    a_r = [a[i] for i in range(mid + 1, r + 1)]
    a_r.append(1e100)
    i, j = 0, 0
    for k in range(l, r + 1):
        if a_l[i] <= a_r[j]:
            a[k] = a_l[i]
            i += 1
        else:
            a[k] = a_r[j]
            j += 1
            count += len(a_l) - i - 1
    return count

def count_inversion(a):
    return count_inversion_ms(a, 0, len(a) - 1)

class CountInversionTestCase(unittest.TestCase):
    def brute_force(self, a):
        count = 0
        for i in range(len(a)):
            for j in range(i + 1, len(a)):
                if a[i] > a[j]:
                    count += 1
        return count

    def random_array(self):
        return [random.randint(0, 100) for _ in range(random.randint(1, 100))]

    def test_empty(self):
        self.assertEqual(count_inversion([]), 0)

    def test_no_inversion(self):
        self.assertEqual(count_inversion([1, 2, 3, 4, 5]), 0)

    def test_all_inversion(self):
        self.assertEqual(count_inversion([5, 4, 3, 2, 1]), 10)

    def test_example(self):
        self.assertEqual(count_inversion([2, 3, 8, 6, 1]), 5)

    def test_equal(self):
        self.assertEqual(count_inversion([2, 4, 3, 3, 4, 2]), 6)

    def test_random(self):
        for _ in range(10000):
            a = self.random_array()
            count = self.brute_force(a)
            self.assertEqual(count_inversion(a), count)

if __name__ == '__main__':
    unittest.main()