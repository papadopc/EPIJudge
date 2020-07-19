from typing import Iterator, List
import heapq
from test_framework import generic_test


def online_median(sequence: Iterator[int]) -> List[float]:
    upper_min_heap = []
    lower_max_heap = []
    results  = []
    for elem in sequence:
        heapq.heappush(lower_max_heap, -heapq.heappushpop(upper_min_heap, elem))
        if len(lower_max_heap)>len(upper_min_heap):
            heapq.heappush(upper_min_heap, -heapq.heappop(lower_max_heap))
        results.append(0.5*(-lower_max_heap[0]+upper_min_heap[0]) if len(upper_min_heap)==len(lower_max_heap) else upper_min_heap[0])
    return results


def online_median_wrapper(sequence):
    return online_median(iter(sequence))


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('online_median.py', 'online_median.tsv',
                                       online_median_wrapper))
