from typing import List
import bisect
from test_framework import generic_test


def intersect_two_sorted_arrays(A: List[int], B: List[int]) -> List[int]:
    def is_present(k):
        i = bisect.bisect_left(B,k)
        return i < len(B) and B[i] == k
    return [a for i, a in enumerate(A) if (i==0 or a != A[i-1]) and is_present(a)]


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('intersect_sorted_arrays.py',
                                       'intersect_sorted_arrays.tsv',
                                       intersect_two_sorted_arrays))
