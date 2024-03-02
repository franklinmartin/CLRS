import random
import unittest

#merge sort modifications
#determine # of inversions in any permutation of n elements
#def count_inversion_sub(arr):

def brute_force(arr):
    inv = []
    cnt = 0
    for i in range (0, len(arr) - 1):
        for j in range(i + 1, len(arr)):
            if(arr[i] > arr[j]):
                inv.append([arr[i], arr[j]])
                cnt += 1

brute_force([2, 3, 8, 6, 1])