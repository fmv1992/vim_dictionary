" Test that the PymodeLintAuto changes a badly formated buffer.

" Load sample python file.
" read ./test_python_sample_code/from_autopep8.py

" Load auxiliary code.
source ./test_helpers_vimscript/vim_dictionary.vim

call VimDictTestWaitForServer()

" call VimDictAddPluginToPythonPath()
let random_words = VimDictGetRandomWords()

" To have at least one valid word.
Dictionary knight

let i = 0
for random_entry in random_words
    echom "Looping in lookup2 with " . i .": " . random_entry
    execute "Dictionary " . random_entry
    let i = i + 1
    sleep 5
endfor

call VimDictClose()

call VimDictFinishTest()
