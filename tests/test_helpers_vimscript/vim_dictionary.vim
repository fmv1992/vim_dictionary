function! VimDictTestWaitForServer() " {{{

    " let l:i = 0
    while ! exists('g:vim_dictionary_channel')
        sleep 50 m
        " let l:i = l:i + 1
        " echom l:i
    endwhile

endfunction
" }}}

function! VimDictGetRandomWords() " {{{

    python3 << EOF
import random
import string
import sys
import logging
logging.disable(sys.maxsize)
# logging.basicConfig(level=logging.CRITICAL)  # Stop logging from showing.
import vim
from vim_dictionary_test import get_random_entries

# N will be doubled because mixed_entries = random_entries + garbage_entries.
N = 10
random_entries = [x.lower() for x in get_random_entries(N)]

MAX_LETTERS = len(string.ascii_letters)
garbage_entries = [''.join(
    random.sample(string.ascii_letters, random.randint(1, MAX_LETTERS)))
    for x in range(N)]

mixed_entries = random_entries + garbage_entries
random.shuffle(mixed_entries)

cb = vim.current.buffer
cb.vars['dict_random_entries'] = mixed_entries
EOF

    return b:dict_random_entries

endfunction

" }}}

function! VimDictGetNthEntry(entry_nr) " {{{

    let b:entry_nr = a:entry_nr

    python3 << EOF
import sys
import logging
logging.disable(sys.maxsize)
import vim
from vim_dictionary_test import get_nth_entry

cb = vim.current.buffer
entry_nr = cb.vars['entry_nr']
cb.vars['dict_nth_entry'] = get_nth_entry(entry_nr)
EOF

    return b:dict_nth_entry

endfunction

" }}}

function! VimDictWaitForDictionaryToClose() " {{{

    " Wait for dictionary to close.
    let chstatus = ch_status(g:vim_dictionary_channel)
    while chstatus == "open"
        let chstatus = ch_status(g:vim_dictionary_channel)
        echom 'chstatus ' . chstatus
        sleep 100 m
    endwhile

endfunction

" }}}

function! VimDictClose() " {{{

    Dictionary !CLOSE

    call VimDictWaitForDictionaryToClose()

endfunction

" }}}

function! VimDictFinishTest() " {{{

    if len(v:errors) > 0
        echom "Exiting lookup1 with errors" . join(v:errors, '|')
        cquit!
    else
        qall!
    endif

endfunction

" }}}

function! VimDictGetRandomNumber(lower, upper) " {{{

    python3 << EOF
import random
import vim

cb = vim.current.buffer

lower = vim.eval('a:lower')
upper = vim.eval('a:upper')

cb.vars['random_value'] = random.randint(int(lower), int(upper))

EOF

    return b:random_value

endfunction

" }}}

function! VimDictGetMaxLineLenForEntry(entry) " {{{

    silent! execute "bdelete! " . bufnr("vim_dictionary-scratch")

    let current_buffer_number = bufnr("%")

    execute "Dictionary " . a:entry

    while bufnr("vim_dictionary-scratch") == -1
        sleep 100
        echom "waiting..."
    endwhile

    execute "buffer! " . bufnr("vim_dictionary-scratch")

    call assert_true(bufnr("vim_dictionary-scratch") == bufnr('%'))
    let line_lengths = []
    for line_number in range(1, line('$'))
        call add(line_lengths, strchars(getline(line_number)))
    endfor
    let max_line_len = max(line_lengths)

    execute "buffer! " . current_buffer_number
    call assert_true(bufnr("%") == current_buffer_number)

    silent! execute "bdelete! " . bufnr("vim_dictionary-scratch")

    return max_line_len

endfunction

" }}}
