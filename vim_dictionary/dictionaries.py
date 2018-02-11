"""Define the available dictionaries.

1. All dictionaries are subclasses of VimDictionary.
2. All dictionaries have a method `lookup` which takes a string and returns a
pretty looking string.

"""

import re

from download_dictionary import DICTIONARY_PATH

from vim_dictionary import instantiate_logger

# pylama: ignore=D101,D102


class VimDictionary(object):
    pass


class WebsterDictionary(VimDictionary):

    # Dict entries in 'websters_unabridged_dictionary_by_various.txt' are all
    # case words (some have space) in a single line.
    DICT_ENTRY_REGEX = re.compile(r'^[A-Z ;-]+$', flags=(re.MULTILINE
                                                         | re.VERBOSE))
    ENTRY_STRING_PATTERN = r'^{0}$.+?(?=^{1}$)'

    def __init__(self):
        self.entries = self._get_entries()

    @staticmethod
    def _get_dictionary():
        """Load dictionary from file.

        Returns:
            str: the loaded dictionary as string.

        """
        def _truncate_dictionary(mydict):
            """Trim dictionary's last 'legal' section."""
            END_OF_DICT = "End of Project Gutenberg's"
            mydict = mydict[0:mydict.index(END_OF_DICT)].strip()
            return mydict

        def _add_last_dummy_entry(mydict):
            """Add a last dummy entry to the dictionary."""
            LAST_DUMMY_ENTRY = '\n' + 100 * 'Z'
            return mydict + LAST_DUMMY_ENTRY

        getdict_logger = instantiate_logger('get_dictionary')
        getdict_logger.debug("Was called.")
        with open(DICTIONARY_PATH, 'rt', encoding='utf8') as f:
            dictionary = f.read()
        dictionary = _truncate_dictionary(dictionary)
        dictionary = _add_last_dummy_entry(dictionary)
        return dictionary

    _RAW_DICTIONARY = _get_dictionary.__func__()

    def _get_entries(self):
        """Get all entries in the dictionary.

        Arguments:
            dictionary (str): the dictionary full text.

        Returns:
            tuple: a tuple of all the entries in the dictionary. In this case
            their order is important as one entry ends where another starts.

        """
        getentries_logger = instantiate_logger('get_entries')
        getentries_logger.debug("Was called.")
        return tuple(self.DICT_ENTRY_REGEX.findall(
            self._RAW_DICTIONARY))

    def lookup(self, entry):
        """Lookup an entry in the dictionary.

        Arguments:
            entry (str): the entry to be looked up.
            dictionary (str): the full dictionary.

        Returns:
            str: the full text of the entry.

        """
        # TODO: improve matching: see 'X RAYS; X-RAYS' for example.
        lookup_logger = instantiate_logger('Lookup')
        next_different_entry = self._get_next_different_entry(entry)
        lookup_logger.debug(
            "Next different entry: '{0}'.".format(next_different_entry))
        if next_different_entry:
            PATTERN = self.ENTRY_STRING_PATTERN.format(
                entry, next_different_entry)
            lookup_logger.debug("pattern: '{0}'.".format(PATTERN))
            full_entry = re.search(
                PATTERN,
                self._RAW_DICTIONARY,
                flags=(re.MULTILINE | re.DOTALL))
            log_result = repr(full_entry.group())
            TRUNCATE_CHARS = 100
            lookup_logger.debug("Truncated entry ({0} chars): '{1}'".format(
                TRUNCATE_CHARS,
                log_result[:min((TRUNCATE_CHARS, len(log_result)))]))
            return full_entry.group().strip()
        else:
            return "'{0}' not in the dictionary.".format(entry)

    def _get_next_different_entry(self, entry):
        """Get next different entry.

        Get next different entry (an entry may have multiple definitions).

        """
        diffentry_logger = instantiate_logger('_get_next_different_entry')
        diffentry_logger.debug("Got '{0}'.".format(entry))
        try:
            first_occurrence = self.entries.index(entry)
        except ValueError as error:
            diffentry_logger.debug(
                "'{0}' is not in the dictionary.".format(entry))
            return ''
        i = first_occurrence + 1
        while self.entries[i] == entry:
            i += 1
        return self.entries[i]

    def __len__(self):
        """Define the result of the builtin 'len' function."""
        return len(self.entries)


class WikitionaryDictionary(VimDictionary):
    pass
