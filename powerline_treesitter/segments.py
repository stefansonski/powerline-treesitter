# vim:fileencoding=utf-8:noet
from __future__ import (unicode_literals, division, absolute_import,
                        print_function)

try:
    import vim
except ImportError:
    vim = object()


def treesitter(pl):
    '''Return treesitter status for the current position.
    Highlight groups used: ``treesitter_identifier`` or ``file_name``.
    '''
    winwidth = vim.eval('nvim_win_get_width(0)')
    treesitter_status = vim.eval('nvim_treesitter#statusline(' + winwidth + ')')
    pl.debug('Current nvim_treesitter#statusline(): %s.' % treesitter_status)
    return [{
        'contents': treesitter_status,
        'highlight_groups': ['treesitter_status', 'file_name']
    }]
