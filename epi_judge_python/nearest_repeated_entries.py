from typing import List
from collections import namedtuple
from test_framework import generic_test


def find_nearest_repetition(paragraph: List[str]) -> int:
    word_to_latest_int = {}
    min_dist = float('inf')
    for i,word in enumerate(paragraph):
        if word in word_to_latest_int:
            min_dist = min(min_dist,i-word_to_latest_int[word])
        word_to_latest_int[word] = i
    if min_dist!=float('inf'):
        return min_dist
    else:
        return -1


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('nearest_repeated_entries.py',
                                       'nearest_repeated_entries.tsv',
                                       find_nearest_repetition))
