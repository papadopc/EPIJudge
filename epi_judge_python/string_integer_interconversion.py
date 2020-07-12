from test_framework import generic_test
from test_framework.test_failure import TestFailure


def int_to_string(x: int) -> str:
    if x<0:
        sign = "-"
    else:
        sign = ""
    x = abs(x)
    digits = []
    if x == 0:
        return "0"
    while x>0:
        digits.append(chr(ord('0')+x%10))
        x=x//10
    retval = sign+"".join(reversed(digits))
    return retval


def string_to_int(s: str) -> int:
    string_digits = "0123456789"
    if s[0] == "-":
        sign = -1
        s = s[1:]
    elif s[0] == "+":
        sign = 1
        s = s[1:]
    else:
        sign = 1
    running_sum = 0
    for char in s:
        running_sum = running_sum*10 + string_digits.index(char)
    return sign*running_sum


def wrapper(x, s):
    if int(int_to_string(x)) != x:
        raise TestFailure('Int to string conversion failed')
    if string_to_int(s) != x:
        raise TestFailure('String to int conversion failed')


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('string_integer_interconversion.py',
                                       'string_integer_interconversion.tsv',
                                       wrapper))
