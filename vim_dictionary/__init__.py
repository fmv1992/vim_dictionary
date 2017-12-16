"""Define dictionary related functions for the vim_dictionary application."""

import logging
import os
import re
import tempfile

# Important: Bottom of file import to avoid cyclic import.
# from download_dictionary import DICTIONARY_PATH

# Dict entries in 'websters_unabridged_dictionary_by_various.txt' are all case
# words (some have space) in a single line.
DICT_ENTRY_REGEX = re.compile(r'^[A-Z ;-]+$', flags=(re.MULTILINE | re.VERBOSE))
ENTRY_STRING_PATTERN = r'^{0}$.+?(?=^{1}$)'

LOGGING_FORMAT = logging.Formatter(
    fmt=('|Thread: %{threadName:s}|{levelname:8s}|{asctime:s}|{name:8s}'
         '| {message:s}'),
    datefmt='%Y-%m-%d %H:%M:%S',
    style='{')


def get_dictionary():
    """Load dictionary from file.

    Returns:
        str: the loaded dictionary as string.

    """
    getdict_logger = _instantiate_logger('get_dictionary')
    getdict_logger.debug("Was called.")
    with open(DICTIONARY_PATH, 'rt', encoding='utf8') as f:
        dictionary = f.read()
    dictionary = _truncate_dictionary(dictionary)
    dictionary = _add_last_dummy_entry(dictionary)
    return dictionary


def _truncate_dictionary(mydict):
    """Trim dictionary's last 'legal' section."""
    END_OF_DICT = "\n+^End of Project Gutenberg's.*"
    mydict = re.sub(END_OF_DICT, '', mydict, flags=(re.DOTALL))
    return mydict


def _add_last_dummy_entry(mydict):
    """Add a last dummy entry to the dictionary."""
    LAST_DUMMY_ENTRY = '\n' + 100 * 'Z'
    return mydict + LAST_DUMMY_ENTRY


def get_entries(dictionary):
    """Get all entries in the dictionary.

    Arguments:
        dictionary (str): the dictionary full text.

    Returns:
        tuple: a tuple of all the entries in the dictionary. In this case their
        order is important as one entry ends where another starts.

    """
    getentries_logger = _instantiate_logger('get_entries')
    getentries_logger.debug("Was called.")
    return tuple(DICT_ENTRY_REGEX.findall(dictionary))


def lookup(entry, entries, dictionary):
    """Lookup an entry in the dictionary.

    Arguments:
        entry (str): the entry to be looked up.
        entries (tuple): a tuple containing all the entries in the dictionary.
        dictionary (str): the full dictionary.

    Returns:
        str: the full text of the entry.

    """
    # TODO: improve matching: see 'X RAYS; X-RAYS' for example.
    lookup_logger = _instantiate_logger('Lookup')
    next_different_entry = _get_next_different_entry(entry, entries)
    lookup_logger.debug(
        "Next different entry: '{0}'.".format(next_different_entry))
    if next_different_entry:
        PATTERN = ENTRY_STRING_PATTERN.format(entry, next_different_entry)
        lookup_logger.debug("pattern: '{0}'.".format(PATTERN))
        full_entry = re.search(
            PATTERN,
            dictionary,
            flags=(re.MULTILINE | re.DOTALL))
        log_result = repr(full_entry.group())
        TRUNCATE_CHARS = 100
        lookup_logger.debug("Truncated entry ({0} chars): '{1}'".format(
            TRUNCATE_CHARS,
            log_result[:min((TRUNCATE_CHARS, len(log_result)))]))
        return full_entry.group().strip()
    else:
        return "'{0}' not in the dictionary.".format(entry)


def _get_next_different_entry(entry, entries):
    """Get next different entry (an entry may have multiple definitions)."""
    diffentry_logger = _instantiate_logger('_get_next_different_entry')
    diffentry_logger.debug("Got '{0}'.".format(entry))
    try:
        first_occurrence = entries.index(entry)
    except ValueError as error:
        diffentry_logger.debug("'{0}' is not in the dictionary.".format(entry))
        return ''
    i = first_occurrence + 1
    while entries[i] == entry:
        i += 1
    return entries[i]


def setup_logging():
    """Set up logging.

    Returns:
        logging.Logger: A logger instantiated with '__name__'.

    """
    logfile = os.path.join(tempfile.gettempdir(), 'vim_dictionary.log')
    logging.basicConfig(
        level=logging.INFO,
        filename=logfile,
        filemode='a')

    rootlogger = _instantiate_logger(__name__)
    rootlogger.debug('Started logging.')
    rootlogger.debug('Logging file is: {0}'.format(logfile))

    return rootlogger


def _instantiate_logger(name):
    # Instantiate logger.
    mylogger = logging.getLogger(name)
    mylogger.setLevel(logging.DEBUG)

    if not mylogger.handlers:
        # Add a console logger as well.
        myconsole = logging.StreamHandler()
        myconsole.setFormatter(LOGGING_FORMAT)
        myconsole.setLevel(logging.DEBUG)
        mylogger.addHandler(myconsole)

    return mylogger


from download_dictionary import DICTIONARY_PATH
