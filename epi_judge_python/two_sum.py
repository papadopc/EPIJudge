from typing import List

from test_framework import generic_test


def has_two_sum(A: List[int], t: int) -> bool:
    num_dict = {}
    for a in A:
        num_dict[a] =1
        if t-a in num_dict:
            return True
    return False


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('two_sum.py', 'two_sum.tsv',
                                       has_two_sum))
