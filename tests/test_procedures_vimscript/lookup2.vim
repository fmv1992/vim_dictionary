" Test that the PymodeLintAuto changes a badly formated buffer.

" Load sample python file.
" read ./test_python_sample_code/from_autopep8.py

" Load auxiliary code.
source ./test_helpers_vimscript/vim_dictionary.vim

call VimDictTestWaitForServer()

" call VimDictAddPluginToPythonPath()
let random_words = VimDictGetRandomWords()

for random_entry in random_words
    execute "Dictionary " . random_entry
endfor

if len(v:errors) > 0
    cquit!
else
    qall!
endif
