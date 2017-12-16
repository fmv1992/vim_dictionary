"""Download dictionary for the vim_dictionary application."""

import os
import urllib.request

from __init__ import _instantiate_logger, setup_logging

DICTIONARY_PATH = os.path.abspath(os.path.join(
    os.path.dirname(os.path.dirname(
        os.path.abspath(__file__))),
    'download',
    'websters_unabridged_dictionary_by_various.txt.utf-8'
))
DICT_URL = 'http://www.gutenberg.org/ebooks/29765.txt.utf-8'


def download_dictionary():
    """Download dictionary to download/ folder.

    Returns:
        None.

    """
    download_logger = _instantiate_logger('download_dictionary')
    download_logger.debug("Opening URL '{0}'.".format(DICT_URL))
    response = urllib.request.urlopen(DICT_URL)
    download_logger.debug("Downloading '{0}'.".format(DICT_URL))
    dictionary_data = response.read()
    with open(DICTIONARY_PATH, 'wb') as f:
        f.write(dictionary_data)
        download_logger.debug("Saved to file '{0}'.".format(DICTIONARY_PATH))


def main():
    """Invoke logging and download the dictionary.

    Returns:
        None.

    """
    setup_logging()
    main_logger = _instantiate_logger('main_logger')
    main_logger.debug('Started logger.')
    download_dictionary()


if __name__ == '__main__':
    main()
