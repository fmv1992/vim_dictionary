"""Define dictionary related functions for the vim_dictionary application."""

import logging
import os
import tempfile

# Important: Bottom of file import to avoid cyclic import.
# from download_dictionary import DICTIONARY_PATH


LOGGING_FORMAT = logging.Formatter(
    fmt=('|Thread: %{threadName:s}|{levelname:8s}|{asctime:s}|{name:8s}'
         '| {message:s}'),
    datefmt='%Y-%m-%d %H:%M:%S',
    style='{')


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
