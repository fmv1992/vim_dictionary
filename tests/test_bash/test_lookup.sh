#! /bin/bash

# Test vim_dictoinary lookups.

# Source file.
set +e
RETURN_CODE=$(vim -i NONE -u $VIM_TEST_VIMRC -c "source ./test_procedures_vimscript/lookup1.vim" $VIM_DISPOSABLE_PYFILE > /dev/null 2>&1)
R1=$?
bash ./test_helpers_bash/test_prepare_between_tests.sh
RETURN_CODE=$(vim -i NONE -u $VIM_TEST_VIMRC -c "source ./test_procedures_vimscript/lookup2.vim" $VIM_DISPOSABLE_PYFILE > /dev/null 2>&1)
R2=$?
bash ./test_helpers_bash/test_prepare_between_tests.sh
RETURN_CODE=$(vim -i NONE -u $VIM_TEST_VIMRC -c "source ./test_procedures_vimscript/lookup3.vim" $VIM_DISPOSABLE_PYFILE > /dev/null 2>&1)
R3=$?

set -e
if [[ "$R1" -ne 0 ]]
then
    exit 1
elif [[ "$R2" -ne 0 ]]
then
    exit 2
elif [[ "$R3" -ne 0 ]]
then
    exit 3
fi

exit 0

# vim: set fileformat=unix filetype=sh wrap tw=0 :
