" Test simple dictionary lookups.

" Load auxiliary code.
source ./test_helpers_vimscript/vim_dictionary.vim

call VimDictTestWaitForServer()


" Invoke the defined command a couple of times.
call assert_true( ! bufexists('vim_dictionary-scratch'))
Dictionary knight
call assert_true(bufexists('vim_dictionary-scratch'))
Dictionary snake
call assert_true(bufexists('vim_dictionary-scratch'))
Dictionary cattle
call assert_true(bufexists('vim_dictionary-scratch'))
Dictionary non existent
call assert_true(bufexists('vim_dictionary-scratch'))

if len(v:errors) > 0
    cquit!
else
    qall!
endif
