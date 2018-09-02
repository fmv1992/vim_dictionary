" Test testwidth enforcement.

" Load auxiliary code.
source ./test_helpers_vimscript/vim_dictionary.vim

" Wait for server to be up.
call VimDictTestWaitForServer()

" Get current buffer number.
let current_file_name = tempname()
" Save the file so it will have a determined buffer number.
execute "write! " . current_file_name
let current_buffer_number = bufnr('%')

" First part: test with textwidth equal to zero.
set textwidth=0
let max_line_length = VimDictGetMaxLineLenForEntry('knight')
call assert_true(max_line_length > 80)
call assert_true(current_buffer_number == bufnr('%'))

" Second part: test with non zero.
let tries = 3
let i = 0
while i < tries
    let random_width = VimDictGetRandomNumber(10, 100)
    execute "set textwidth=" . random_width
    echom "Textwidth is '" . &tw . "'."
    let max_line_length = VimDictGetMaxLineLenForEntry('knight')
    echom "Max found textwidth is '" . max_line_length . "'."
    call assert_true(max_line_length <= &tw)
    call assert_true(current_buffer_number == bufnr('%'))
    let i = i + 1
    redraw!
    sleep 5000 m
endwhile

call VimDictClose()

call VimDictFinishTest()
