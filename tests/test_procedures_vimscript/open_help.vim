" Open help.

" Load auxiliary code.
source ./test_helpers_vimscript/vim_dictionary.vim

call VimDictTestWaitForServer()

try
    help vim_dictionary
catch /^Vim\%((\a\+)\)\=:E149/
    cquit!
endtry
qall!
