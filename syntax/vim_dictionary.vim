" Define new highlighting group similar. {{{
highlight! vimdictionaryBoldType term=underline ctermfg=67 guifg=#5f87af
    \ cterm=bold
" }}}

" Define syntaxes highilighting. {{{
syntax match vimdictionary_title /^[A-Z]\+$/

syntax match vimdictionary_definition /^[0-9]\+\./

syntax match vimdictionary_definition /^([a-z])/
syntax match vimdictionary_definition /^[Dd]efn:/
" }}}

" Link to defined/existing highlight groups. See ':highlight' for details. {{{
highlight link vimdictionary_title vimdictionaryBoldType
highlight link vimdictionary_definition Statement
" }}}
