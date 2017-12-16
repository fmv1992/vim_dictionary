#! /bin/bash

# Test vim_dictoinary lookups.

# Source file.
set +e
RETURN_CODE=$(vim -i NONE -u $VIM_TEST_VIMRC -c "source ./test_procedures_vimscript/open_help.vim" $VIM_DISPOSABLE_PYFILE > /dev/null 2>&1)
R1=$?
set -e

if [[ "$R1" -ne 0 ]]
then
    exit 1
fi

exit 0

# vim: set fileformat=unix filetype=sh wrap tw=0 :
