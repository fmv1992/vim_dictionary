"""Provide functions to test this plugin."""

import unittest

import random

from dictionaries import WebsterDictionary


class WebsterDictionaryTest(unittest.TestCase):
    """Unit test for WebsterDictionary."""
    pass


def get_random_entries(n_sample=10):
    """Get a list of random entries."""
    dictionary = WebsterDictionary()
    return random.sample(dictionary.entries, n_sample)


def get_nth_entry(n):
    """Get the nth entry from the dictionary."""
    # Correct the dummy last placed entry 'ZZZ...'.
    if n < 0:
        n -= 1
    dictionary = WebsterDictionary()
    all_entries = dictionary.entries
    return all_entries[n]
