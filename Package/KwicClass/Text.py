from functools import cmp_to_key
from Package.KwicClass.LinesSortRule_Context import LinesSortContext
from Package.KwicClass.LinesSearchRule_Context import LinesSearchContext

class Text(object):
    def __init__(self):
        self.lines = []

    def addLine(self, line):
        self.lines.append(line)

    def clear(self):
        self.lines = []

    def cyclicShift(self):
        for line in self.lines:
            line.cyclicShift()

    def setSortRule(self,sort_rule):
        self.sort_context = LinesSortContext(sort_rule)

    def sort(self):
        self.lines = sorted(self.lines, key=cmp_to_key(self.sort_context.cmp))

    def setSearchRule(self,search_rule):
        self.search_context = LinesSearchContext(search_rule)

    def search(self,keywords):
        return self.search_context.search(self.lines,keywords)

    def toString(self):
        sentences = []
        for line in self.lines:
            sentences.append(line.sentence)
        return '\n'.join(sentences)
