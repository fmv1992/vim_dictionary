#! /bin/bash

# Check before starting.
set -e
which vim 1>/dev/null 2>/dev/null

# Go to test root directory.
cd $(dirname $0)

# Source common variables.
source ./test_helpers_bash/test_variables.sh

# Prepare tests by cleaning up all files.
source ./test_helpers_bash/test_prepare_once.sh

# Initialize permanent files..
source ./test_helpers_bash/test_createvimrc.sh

# Execute tests.
# TODO: enable those commented out tests.
declare -a TEST_ARRAY=(
"./test_bash/test_lookup.sh"
"./test_bash/test_helpfiles.sh"
# "./test_bash/test_download.sh"
# "./test_bash/test_server.sh"
)
declare -a DICTIONARIES=(
"--dictionary webster"
"--dictionary wikitionary"
)
## now loop through the above array
set +e
for ONE_DICTIONARY in "${DICTIONARIES[@]}"
do
    eval "python3 ../vim_dictionary/vim_dictionary_server.py $ONE_DICTIONARY &"
    for ONE_TEST in "${TEST_ARRAY[@]}"
    do
        echo "Starting test: $ONE_TEST" >> $VIM_OUTPUT_FILE
        bash -x "$ONE_TEST"
        echo -e "\n$ONE_TEST: Return code: $?" >> $VIM_OUTPUT_FILE
        bash ./test_helpers_bash/test_prepare_between_tests.sh
    done
    bash ./test_helpers_bash/test_kill_server.sh
    sleep 10s
done
set -e

# Show errors:
E1=$(grep -E "^E[0-9]+:" $VIM_OUTPUT_FILE)
E2=$(grep -E "^Error" $VIM_OUTPUT_FILE)
E3="$E1\n$E2"
if [ "$E3" = "\n" ]
then
    echo "No errors."
else
    echo "Errors:"
    echo -e "$E3\n"
fi

# Show return codes.
RETURN_CODES=$(cat $VIM_OUTPUT_FILE | grep -i "Return code")
echo -e "${RETURN_CODES}"

# Exit the script with error if there are any return codes different from 0.
if echo $RETURN_CODES | grep -E "Return code: [1-9]" 1>/dev/null 2>/dev/null
then
    echo "Terminating with errors."
    exit 1
else
    echo "Terminating without errors."
    exit 0
fi

# vim: set fileformat=unix filetype=sh wrap tw=0 :
