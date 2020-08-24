if get(s:, 'loaded', 0)
  finish
endif
let s:loaded = 1
let g:ncm2_calc#mark = get(g:, 'ncm2_calc#mark', 'calc')
let g:ncm2_calc#proc = yarp#py3({
      \ 'module': 'ncm2_calc',
      \ 'on_load': { -> ncm2#set_ready(g:ncm2_calc#source)}
      \ })
let g:ncm2_calc#calc_source = get(g:, 'ncm2_calc#calc_source', {
      \ 'name': 'calc',
      \ 'priority': 10,
      \ 'ready': 0,
      \ 'complete_length': 3,
      \ 'mark': g:ncm2_calc#mark,
      \ 'word_pattern': '(?:\\d+(?:\\.\\d+)?|\\s*)+$',
      \ 'on_complete': 'ncm2_calc#on_complete',
      \ })
let g:ncm2_calc#source = extend(g:ncm2_calc#calc_source,
      \ get(g:, 'ncm2_calc#source_override', {}),
      \ 'force')
function! ncm2_calc#init() abort
  call ncm2#register_source(g:ncm2_calc#source)
endfunction
function! ncm2_calc#on_complete(ctx) abort
  call g:ncm2_calc#proc.try_notify('on_complete', a:ctx)
endfunction
