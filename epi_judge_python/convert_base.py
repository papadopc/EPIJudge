from test_framework import generic_test
import functools

def convert_base(num_as_string: str, b1: int, b2: int) -> str:
    digits_hex = '0123456789ABCDEF'

    def construct_from_base(num_as_int,base):
        return ('' if num_as_int == 0 else
                construct_from_base(num_as_int//base, base)+digits_hex[num_as_int % base])
    is_negative = num_as_string[0] == "-"
    num_as_int = functools.reduce(lambda x,c: x*b1+digits_hex.index(c.upper()), num_as_string[is_negative:], 0)
    return ('-' if is_negative else '') + ('0' if num_as_int==0 else construct_from_base(num_as_int, b2))


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('convert_base.py', 'convert_base.tsv',
                                       convert_base))
