from typing import List

from test_framework import generic_test, test_utils
import collections


def find_anagrams(dictionary: List[str]) -> List[List[str]]:
    anagram_dict = collections.defaultdict(list)
    for word in dictionary:
        anagram_dict["".join(sorted(word))]+= [word]
    result = []
    for key in anagram_dict:
        if len(anagram_dict[key])>1:
            result.append(anagram_dict[key])
    return result


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            'anagrams.py',
            'anagrams.tsv',
            find_anagrams,
            comparator=test_utils.unordered_compare))
