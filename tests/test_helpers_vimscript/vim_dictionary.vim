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

N = 20
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
