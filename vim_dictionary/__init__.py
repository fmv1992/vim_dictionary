"""Define dictionary related functions for the vim_dictionary application."""

from collections import namedtuple
import argparse
import logging
import os
import tempfile

try:
    import wiktionaryparser  # noqa
    HAS_WIKITIONARY = True
except ImportError:
    HAS_WIKITIONARY = False

# Important: Bottom of file import to avoid cyclic import.
# from download_dictionary import DICTIONARY_PATH


MESSAGE_CONTENT_SEPARATOR = '|'  # Counterpart to l:separator.
MessageContent = namedtuple('message_content', ['lookup_word', 'textwidth'])


LOGGING_FORMAT = logging.Formatter(
    fmt=('|Thread: %{threadName:18s}|{levelname:8s}|{asctime:s}|{name:12s}'
         '| {message:s}'),
    datefmt='%Y-%m-%d %H:%M:%S',
    style='{')


def parse_arguments():
    """Parse arguments."""
    parser = argparse.ArgumentParser()
    parser.add_argument(
        '--dictionary',
        help=("Set the dictionary to be used. Implemented options are: "
              "{0}.".format(",".join(["'wikitionary' (online)",
                                      "'webster' (offline)"]))),
        default='wikitionary',
        required=True)

    args = parser.parse_args()

    return args


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

    rootlogger = instantiate_logger(__name__)
    rootlogger.debug('Started logging.')
    rootlogger.debug('Logging file is: {0}'.format(logfile))

    return rootlogger


def instantiate_logger(name):
    """Instatite a logger."""
    mylogger = logging.getLogger(name)
    mylogger.setLevel(logging.DEBUG)

    if not mylogger.handlers:
        # Add a console logger as well.
        myconsole = logging.StreamHandler()
        myconsole.setFormatter(LOGGING_FORMAT)
        myconsole.setLevel(logging.DEBUG)
        mylogger.addHandler(myconsole)

    return mylogger


def get_dictionary():
    """Return the dictionary read from the command line arguments."""
    from dictionaries import WebsterDictionary,  WikitionaryDictionary
    arguments = parse_arguments()
    if arguments.dictionary == 'webster':
        dictionary = WebsterDictionary()
    elif arguments.dictionary == 'wikitionary':
        dictionary = WikitionaryDictionary()
    return dictionary
