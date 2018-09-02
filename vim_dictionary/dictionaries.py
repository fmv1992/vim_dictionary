"""Define the available dictionaries.

1. All dictionaries are subclasses of VimDictionary.
2. All dictionaries have a method `lookup` which takes a string and returns a
pretty looking string.

"""

import textwrap
import re

from wiktionaryparser import WiktionaryParser

from download_dictionary import DICTIONARY_PATH
import __init__ as vim_dictionary


class VimDictionary(object):
    """General dictionary interface."""

    def format_looked_up_word(self, list_of_paragraphs, textwidth):
        """Join wrapped paragraphs by empty lines."""
        if textwidth:
            fill_function = lambda x: textwrap.fill(x, width=textwidth)
        else:
            fill_function = lambda x: x
        return '\n\n'.join(map(fill_function, list_of_paragraphs))

    def lookup(self, entry, language, textwidth):
        """Lookup words according to private method '_lookup'."""
        lookup_logger = vim_dictionary.instantiate_logger('Lookup')
        lookup_logger.debug("Looking up: '{0}'".format(entry))
        lines_of_entry = self._lookup(entry, language)
        return self.format_looked_up_word(lines_of_entry, textwidth).strip()


class WebsterDictionary(VimDictionary):
    """Offline dictionary from Guttenberg Project."""

    # Dict entries in 'websters_unabridged_dictionary_by_various.txt' are all
    # case words (some have space) in a single line.
    DICT_ENTRY_REGEX = re.compile(r'^[A-Z ;-]+$', flags=(re.MULTILINE
                                                         | re.VERBOSE))
    ENTRY_STRING_PATTERN = r'^{0}$.+?(?=^{1}$)'

    def __init__(self):
        """Initialize instance."""
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

        getdict_logger = vim_dictionary.instantiate_logger('get_dictionary')
        getdict_logger.debug("Was called.")
        with open(DICTIONARY_PATH, 'rt', encoding='utf8') as f:
            dictionary = f.read()
        dictionary = _truncate_dictionary(dictionary)
        dictionary = _add_last_dummy_entry(dictionary)
        return dictionary

    def _get_entries(self):
        """Get all entries in the dictionary.

        Arguments:
            dictionary (str): the dictionary full text.

        Returns:
            tuple: a tuple of all the entries in the dictionary. In this case
            their order is important as one entry ends where another starts.

        """
        getentries_logger = vim_dictionary.instantiate_logger('get_entries')
        getentries_logger.debug("Was called.")
        self._RAW_DICTIONARY = self._get_dictionary()
        getentries_logger.debug("Set '_RAW_DICTIONARY' attribute.")
        return tuple(self.DICT_ENTRY_REGEX.findall(
            self._RAW_DICTIONARY))

    def _lookup(self, entry, language):
        """Lookup an entry in the dictionary.

        Arguments:
            entry (str): the entry to be looked up.
            dictionary (str): the full dictionary.

        Returns:
            lines (list): list of strings where each string is a paragraph.

        """
        if language != 'english':
            raise ValueError(
                "Looking up the word '{word}' for language '{lang}' with"
                " English only dictionary.".format(
                    word=entry,
                        lang=language))
        entry = entry.upper()
        # TODO: improve matching: see 'X RAYS; X-RAYS' for example.
        next_different_entry = self._get_next_different_entry(entry)
        if next_different_entry:
            PATTERN = self.ENTRY_STRING_PATTERN.format(
                entry, next_different_entry)
            full_entry = re.search(
                PATTERN,
                self._RAW_DICTIONARY,
                flags=(re.MULTILINE | re.DOTALL)).group().strip()
            fe_with_line_between_title_and_body = (
                full_entry[:len(entry)] + '\n' + full_entry[len(entry):])
            return fe_with_line_between_title_and_body.split('\n\n')
        else:
            return ["'{0}' not in the dictionary.".format(entry), ]

    def _get_next_different_entry(self, entry):
        """Get next different entry.

        Get next different entry (an entry may have multiple definitions).

        """
        diffentry_logger = vim_dictionary.instantiate_logger(
            '_get_next_different_entry')
        diffentry_logger.debug("Got '{0}'.".format(entry))
        try:
            first_occurrence = self.entries.index(entry)
        except ValueError:
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


if vim_dictionary.HAS_WIKITIONARY:
    class WikitionaryDictionary(VimDictionary):
        """Online dictionary from wikitionary."""

        def __init__(self):
            """Initialize instance."""
            self._parser = WiktionaryParser()

        def _lookup(self, entry, language):
            """Language is ignored for this dictionary."""
            wikitionary_result = self._parser.fetch(entry, language=language)
            result = self.parse_wikitionary_entry(entry, wikitionary_result)
            return result

        @staticmethod
        def parse_wikitionary_entry(word, wikiresult):
            """Parse wikitionary entry."""
            lines = list()

            for i1, entry in enumerate(wikiresult, start=1):
                lines.append(word.upper() + '\n')
                for i2, definition in enumerate(entry['definitions'], start=1):
                    text = definition['text']
                    # ??? Apply format improvements based on regex such as
                    # capitalization and adding spaces after a '.'.
                    one_line = '{entry_number}. {content}'.format(
                        entry_number=i2,
                        content=text.capitalize())
                    lines.append(one_line)
            return lines
