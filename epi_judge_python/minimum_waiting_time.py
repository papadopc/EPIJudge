from typing import List

from test_framework import generic_test


def minimum_total_waiting_time(service_times: List[int]) -> int:
    service_times.sort()
    retval = 0
    for i, s_t in enumerate(service_times):
        remaining_queries = len(service_times) - (i+1)
        retval += s_t*remaining_queries
    return retval


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('minimum_waiting_time.py',
                                       'minimum_waiting_time.tsv',
                                       minimum_total_waiting_time))
