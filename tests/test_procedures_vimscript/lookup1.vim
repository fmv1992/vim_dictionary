" Test simple dictionary lookups.

" Load auxiliary code.
source ./test_helpers_vimscript/vim_dictionary.vim

call VimDictTestWaitForServer()


" Invoke the defined command a couple of times.
call assert_true( ! bufexists('vim_dictionary-scratch'))
Dictionary knight
Dictionary snake
Dictionary cattle
Dictionary non existent

sleep 10000 m
call assert_true(bufexists('vim_dictionary-scratch'))

call VimDictClose()

call VimDictFinishTest()
