# -*- coding: utf-8 -*-
import re
from ncm2 import Ncm2Source
import vim


class Source(Ncm2Source):
    def __init__(self, vim):
        super(Source, self).__init__(vim)

        self.vars = {}
        self.word_pattern = self.regex()
        self.ignore_pattern = r'^(?:\d+(?:\.\d+)?|\s)+$'
        # self.is_volatile = True
        self.complete_length = 3

    def on_complete(self, context):
        candidates = []
        try:
            calculates = re.findall(self.word_pattern, context['base'])
            if re.match(self.ignore_pattern, calculates[0]):
                return []

            output = str(eval(calculates[0]))
            candidates += [{
                'word':
                ' = {}'.format(output),
                'abbr':
                '{} = {}'.format(calculates[0].strip(), output),
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
        self.complete(context, context['startccol'], candidates)

    def regex(self):
        parts = []
        parts += [r'\d+(?:\.\d+)?']
        parts += [r'\s*']
        parts += [re.escape(x) for x in ['+', '*', '/', '-', '%']]
        parts += [re.escape(x) for x in ['(', ')']]
        regex = r'(?:' + r'|'.join(parts) + r')+$'
        return regex


source = Source(vim)
on_complete = source.on_complete
