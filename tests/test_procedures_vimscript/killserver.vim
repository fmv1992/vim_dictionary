" Test simple dictionary lookups.

" Load auxiliary code.
source ./test_helpers_vimscript/vim_dictionary.vim

call VimDictTestWaitForServer()

Dictionary !CLOSE

let chstatus = ch_status(g:vim_dictionary_channel)
while chstatus == "open"
    let chstatus = ch_status(g:vim_dictionary_channel)
    echom 'chstatus ' . chstatus
    sleep 100 m
endwhile

quit!
