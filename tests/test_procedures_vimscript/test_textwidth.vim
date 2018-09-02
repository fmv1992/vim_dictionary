" Test testwidth enforcement.

" Load auxiliary code.
source ./test_helpers_vimscript/vim_dictionary.vim

" Wait for server to be up.
call VimDictTestWaitForServer()

let entry = 'knight'

set textwidth=0

execute "Dictionary " . entry

sleep 15000 m
call assert_true(bufexists('vim_dictionary-scratch'))

call VimDictClose()

call VimDictFinishTest()
