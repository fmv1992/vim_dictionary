" Python server related functions. {{{
function! vimdictionary#vimdictionaryclose() " {{{
    if ! g:vimdictionary_persistent_server
        let l:vim_pids = s:VimDictGetVimPIDS()
        if len(l:vim_pids) == 1
            " Terminate running python server.
            call ch_evalexpr(g:vim_dictionary_channel, '!close')
        endif
    else
        " Let the python process in the background.
    endif
endfunction

" }}}
function! s:VimDictGetVimPIDS() " {{{

    python3 << EOF
import vim
from subprocess import check_output
cb = vim.current.buffer

PROC_NAME = 'vim'

def get_pids():
    return map(int, check_output(["pidof", PROC_NAME]).split())

cb.vars['vim_pids'] = get_pids()
EOF

    return b:vim_pids

endfunction

" }}}
function! vimdictionary#connecttodictionaryserver(timerid) " {{{
    " Connect to server but do not let vim hanging...

    let g:vim_dictionary_channel = ch_open('localhost:49158')
    " let l:i = 0
    while ch_status(g:vim_dictionary_channel) == 'fail'
        " echom '(' . l:i. ') fail...'
        sleep 100 m
        let g:vim_dictionary_channel = ch_open('localhost:49158')
        " let l:i = l:i + 1
    endwhile

    " echom 'Suceeded!'
    call timer_stop(a:timerid)

endfunction

" }}}
" }}}

" Functions related to dictionary window. {{{
function! vimdictionary#populatedictionarywindow(definition) " {{{
    let l:curr_win_nr = win_getid(winnr())
    call s:VimDictOpenVimDictWindow()
    silent put=a:definition
    normal! gg
    " Delete to black hole register.
    normal! "_dd
    setlocal readonly
    call win_gotoid(l:curr_win_nr)
endfunction

" }}}
function! s:VimDictOpenVimDictWindow() " {{{
    let l:dictionary_buffer_name = 'vim_dictionary-scratch'
    if bufname(l:dictionary_buffer_name) != ''
        execute 'bdelete ' . l:dictionary_buffer_name
    endif
    botright new
    execute ':edit ' . l:dictionary_buffer_name
    setlocal filetype=vim_dictionary
    setlocal nospell
    setlocal buftype=nofile
    setlocal bufhidden=hide
    setlocal noswapfile
    execute 'setlocal winheight=' . g:vimdictionary_winheight
    execute 'setlocal winminheight=' . g:vimdictionary_winminheight
    execute 'resize ' . g:vimdictionary_winheight
endfunction

" }}}
" }}}

" Functions related to dictionary lookup. {{{
function! vimdictionary#getdictionarydefinition(word) " {{{
    let l:definition = ch_evalexpr(g:vim_dictionary_channel, a:word)
    return l:definition
endfunction

" }}}
" }}}

" Functions related to project maintenance. {{{
function! vimdictionary#default(name, default) "{{{
    if ! exists(a:name)
        let {a:name} = a:default
        return 0
    endif
    return 1
endfunction

" }}}
" }}}
