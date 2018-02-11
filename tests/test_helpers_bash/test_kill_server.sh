#! /bin/bash

# Source file.
# set +e
set -e
RETURN_CODE=$(vim -i NONE -u $VIM_TEST_VIMRC -c "source ./test_procedures_vimscript/killserver.vim" > /dev/null 2>&1)
