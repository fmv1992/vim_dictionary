#! /bin/bash

# Test vim_dictoinary lookups.

# Source file.
set -e
vim -i NONE -u $VIM_TEST_VIMRC -c "source ./test_procedures_vimscript/lookup1.vim" $VIM_DISPOSABLE_PYFILE
vim -i NONE -u $VIM_TEST_VIMRC -c "source ./test_procedures_vimscript/lookup2.vim" $VIM_DISPOSABLE_PYFILE

# vim: set fileformat=unix filetype=sh wrap tw=0 :
