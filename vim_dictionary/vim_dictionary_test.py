"""Provide functions to test this plugin."""

import random

from __init__ import DICT_ENTRY_REGEX, get_dictionary


def get_random_entries(n_sample=100):
    """Get a list of random entries."""
    dictionary = get_dictionary()
    all_entries = tuple(DICT_ENTRY_REGEX.findall(dictionary))
    return random.sample(all_entries, n_sample)


def get_nth_entry(n):
    """Get the nth entry from the dictionary."""
    # Correct the dummy last placed entry 'ZZZ...'.
    if n < 0:
        n -= 1
    dictionary = get_dictionary()
    all_entries = tuple(DICT_ENTRY_REGEX.findall(dictionary))
    return all_entries[n]
