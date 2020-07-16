from test_framework import generic_test
from collections import Counter

def is_letter_constructible_from_magazine(letter_text: str,
                                          magazine_text: str) -> bool:
    letter_counter = Counter(letter_text)
    for c in magazine_text:
        if c in letter_counter:
            letter_counter[c] -= 1
            if letter_counter[c] == 0:
                del letter_counter[c]
            if not letter_counter:
                return True
    return not letter_counter


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            'is_anonymous_letter_constructible.py',
            'is_anonymous_letter_constructible.tsv',
            is_letter_constructible_from_magazine))
