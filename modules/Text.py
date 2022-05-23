from functools import cmp_to_key
from LinesSortRule import SpaceAdvance
from LinesSearchRule import LinesSearchContext

class Text(object):
    def __init__(self):
        self.lines = []

    def addLine(self, line):
        self.lines.append(line)

    def sort(self):
        self.sort_rule = SpaceAdvance() #或许可以改成工厂模式,现在这是策略模式？
        self.lines = sorted(self.lines, key=cmp_to_key(self.sort_rule.cmp))

    def search(self,words):
        self.search_context = LinesSearchContext(1)
        return self.search_context.search(self.lines,words)