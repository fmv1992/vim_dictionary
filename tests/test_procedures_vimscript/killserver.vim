" Test simple dictionary lookups.

" Load auxiliary code.
source ./test_helpers_vimscript/vim_dictionary.vim

call VimDictTestWaitForServer()

call VimDictClose()

call VimDictFinishTest()
