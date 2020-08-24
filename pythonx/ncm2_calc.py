# -*- coding: utf-8 -*-
import re
from ncm2 import Ncm2Source
import vim


class Source(Ncm2Source):
    def __init__(self, vim):
        super(Source, self).__init__(vim)

        self.vim = vim
        self.ignore_pattern = r'^(?:\d+(?:\.\d+)?|\s)+$'

    def __print(self, output):
        self.vim.command("python3 print(\"{}\")".format(repr(output)))

    def on_complete(self, context):
        candidates = []
        try:
            # calculates = re.findall(self.word_pattern, context['base'])
            if re.match(self.ignore_pattern, context['base']):
                return []

            output = str(eval(context['base']))
            candidates += [{
                'word':
                ' = {}'.format(output),
                'abbr':
                '{} = {}'.format(context['base'].strip(), output),
                'dup':
                1
            }]
            candidates += [{
                'word': ' = {}'.format(output),
                'abbr': output,
                'dup': 1
            }]
        except:
            pass
        self.complete(context, context['startccol'] + len(context['base']),
                      candidates)


source = Source(vim)
on_complete = source.on_complete
