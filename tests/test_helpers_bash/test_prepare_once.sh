#! /bin/bash

# Prepare tests.
set +e
rm $VIM_OUTPUT_FILE $VIM_TEST_VIMRC $VIM_TEST_VIMDICTCOMMANDS $VIM_DISPOSABLE_PYFILE 2&>/dev/null
set -e

# vim: set fileformat=unix filetype=sh wrap tw=0 :
