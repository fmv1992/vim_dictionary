" Test lookup for first and last entries.

" Load auxiliary code.
source ./test_helpers_vimscript/vim_dictionary.vim

call VimDictTestWaitForServer()

" call VimDictAddPluginToPythonPath()
let first_entry = VimDictGetNthEntry(0)
let last_entry = VimDictGetNthEntry(-1)

execute "Dictionary " . first_entry
execute "Dictionary " . last_entry

if len(v:errors) > 0
    cquit!
else
    qall!
endif
