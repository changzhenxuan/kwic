from functools import cmp_to_key
from Package.KwicClass.LinesSortRule import SpaceAdvance
from Package.KwicClass.LinesSearchRule import LinesSearchContext

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

    def sort(self):
        self.sort_rule = SpaceAdvance() #或许可以改成工厂模式,现在这是策略模式？
        self.lines = sorted(self.lines, key=cmp_to_key(self.sort_rule.cmp))

    def search(self,words):
        self.search_context = LinesSearchContext(1)
        return self.search_context.search(self.lines,words)

    def toString(self):
        sentences = []
        for line in self.lines:
            sentences.append(line.sentence)
        return '\n'.join(sentences)