from test_framework import generic_test


def fibonacci(n: int) -> int:
    if n<=1:
        return n
    a_1, a_2 = 0, 1
    for i in range(1,n):
        a_n = a_1+a_2
        a_1, a_2 = a_2, a_n
    return a_2


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('fibonacci.py', 'fibonacci.tsv',
                                       fibonacci))
