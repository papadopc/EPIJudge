from test_framework import generic_test
from typing import List


def levenshtein_distance(A: str, B: str) -> int:
    distance_between_prefixes: List[List[int]] = [ [-1]*len(B) for _ in range(len(A))]

    def compute_distance_between_prefixes(A_idx, B_idx):
        if A_idx<0:
            return B_idx+1
        if B_idx<0:
            return A_idx+1
        if distance_between_prefixes[A_idx][B_idx] == -1:
            if A[A_idx] == B[B_idx]:
                distance_between_prefixes[A_idx][B_idx] = compute_distance_between_prefixes(A_idx-1,B_idx-1)
            else:
                substitute_last = compute_distance_between_prefixes(A_idx-1, B_idx-1)
                add_last = compute_distance_between_prefixes(A_idx, B_idx-1)
                delete_last = compute_distance_between_prefixes(A_idx-1, B_idx)
                distance_between_prefixes[A_idx][B_idx] = 1+min(substitute_last,add_last,delete_last)
        return distance_between_prefixes[A_idx][B_idx]
    return compute_distance_between_prefixes(len(A)-1,len(B)-1)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('levenshtein_distance.py',
                                       'levenshtein_distance.tsv',
                                       levenshtein_distance))
