## @file
## @brief meta: Hot Backup system in Rust /drafts/

from metaL import *

p = Project(
    title='''Hot Backup system in Rust /drafts/''',
    about='''
https://t.me/rustlang_ru/402212

* Linux host/target only
  * user-space disk volume driver (soft-raid over a network like)
''') \
    | Rust() \
    | Kernel()

p.mk.src \
    // f'{"C":<3} += src/blockio.c' \
    // f'{"S":<3} += $(C)'

p.mk.all_.after(p.mk.all,
                (S('bin/blockio: $(C)', pfx='')
                 // '$(CXX) -o $@ $^ && $@'))

p.doxy.input.value += ' src/blockio.c'

p.sync()
