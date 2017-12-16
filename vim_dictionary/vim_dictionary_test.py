import random
import re

from __init__ import DICT_ENTRY_REGEX, get_dictionary

def get_random_entries(n_sample=100):
    dictionary = get_dictionary()
    all_entries = tuple(DICT_ENTRY_REGEX.findall(dictionary))
    return random.sample(all_entries, n_sample)


def get_nth_entry(n):
    # Correct the dummy last placed entry 'ZZZ...'.
    if n < 0:
        n -= 1
    dictionary = get_dictionary()
    all_entries = tuple(DICT_ENTRY_REGEX.findall(dictionary))
    return all_entries[n]
