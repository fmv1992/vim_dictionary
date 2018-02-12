" Check plugin dependencies. {{{
let s:lack_deps = []
if ! has('python3')
    call add(s:lack_deps, 'python3')
endif
if ! has ('channel')
    call add(s:lack_deps, 'channel')
endif
if len(s:lack_deps) != 0
    echoerr 'vim_dictionary: vim lacks the following dependencies: '
        \ . join(s:lack_deps, ', ')
    finish
endif
" }}}

" Global constants declaration. {{{
let g:vim_dictionary_root = expand('<sfile>:p:h:h') . '/vim_dictionary'
" }}}

" User variables. {{{
" TODO
" }}}

" Set plugin variables. {{{
call vimdictionary#default('g:vimdictionary_dictionary', 'wikitionary')
call vimdictionary#default('g:vimdictionary_persistent_server', 1)
call vimdictionary#default('g:vimdictionary_winheight', 10)
call vimdictionary#default('g:vimdictionary_winminheight', 5)
" }}}

" Functions. {{{
function! s:VimDictInit() " {{{

    call s:VimDictAddPluginToPythonPath()
    if ! s:VimDictCheckServerIsAlive()
        call s:VimDictStartDictionaryServer()
    endif
    call s:VimDictConnectToServer()

endfunction

" }}}
function! s:VimDictAddPluginToPythonPath() " {{{

    python3 import sys, vim
    python3 sys.path.insert(0, vim.eval("g:vim_dictionary_root"))

endfunction

" }}}
function! s:VimDictStartDictionaryServer() " {{{

    let l:py3server_file = g:vim_dictionary_root .
        \ '/vim_dictionary_server.py ' .
        \ '--dictionary ' . g:vimdictionary_dictionary . ' &'
    call system("python3 " . l:py3server_file)

endfunction

" }}}
function! s:VimDictConnectToServer() " {{{

    let l:timer = timer_start(100,
        \ 'vimdictionary#connecttodictionaryserver',
        \ {'repeat': 100})

endfunction

" }}}
function! s:VimDictCheckServerIsAlive() " {{{

    python3 << EOF
import sys
import logging
logging.disable(sys.maxsize)

import vim
from vim_dictionary_server import check_server_is_on

cb = vim.current.buffer

cb.vars['vim_dictionary_server_is_alive'] = check_server_is_on()

EOF

return b:vim_dictionary_server_is_alive

endfunction

" }}}
function! s:VimDictDictionary(word) " {{{
    " Old synchronous/blocking call.
    " let l:definition = vimdictionary#getdictionarydefinition(a:word)
    " call vimdictionary#populatedictionarywindow(l:definition)
    call ch_sendexpr(g:vim_dictionary_channel,
        \ a:word,
        \ {'callback': 'vimdictionary#populatedictionarywindow',
        \ 'timeout': 10000})
endfunction

" }}}
" }}}

" Autocmd-groups. {{{
augroup vimdictionary
    au!
    " Terminate server if closing vim is the last vim instance.
    au VimLeave * call vimdictionary#vimdictionaryclose()
augroup END
" }}}

" Initialize plugin. {{{
call s:VimDictInit()
" }}}

" Define commands. {{{
command! -nargs=1 Dictionary :call s:VimDictDictionary(<f-args>)
" }}}
