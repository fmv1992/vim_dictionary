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

" let chstatus = ch_status(g:vim_dictionary_channel)
" while chstatus == "open"
"     let chstatus = ch_status(g:vim_dictionary_channel)
"     echom 'chstatus ' . chstatus
"     sleep 100 m
" endwhile
sleep 10000 m
call assert_true(bufexists('vim_dictionary-scratch'))

if len(v:errors) > 0
    echom "Exiting lookup1 with errors" . join(v:errors, '|')
    cquit!
else
    qall!
endif
