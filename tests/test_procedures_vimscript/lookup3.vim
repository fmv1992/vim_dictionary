" Test lookup for first and last entries.

" Load auxiliary code.
source ./test_helpers_vimscript/vim_dictionary.vim

call VimDictTestWaitForServer()

" call VimDictAddPluginToPythonPath()
let first_entry = VimDictGetNthEntry(0)
let last_entry = VimDictGetNthEntry(-1)

execute "Dictionary " . first_entry
execute "Dictionary " . last_entry

" let chstatus = ch_status(g:vim_dictionary_channel)
" while chstatus == "open"
"     let chstatus = ch_status(g:vim_dictionary_channel)
"     echom 'chstatus ' . chstatus
"     sleep 100 m
" endwhile
sleep 15000 m
call assert_true(bufexists('vim_dictionary-scratch'))


if len(v:errors) > 0
    echom "Exiting lookup3 with errors" . join(v:errors, '|')
    cquit!
else
    qall!
endif
