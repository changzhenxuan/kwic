from Package.KwicClass.LineSearchRule import LSearch_notin,LSearch_re,LSearch_kmp
from Package.KwicClass import LinesSearchRule_Context
#策略模式：查询策略/规则
class LinesSearchRule(object):
    def __init__(self):
        raise NotImplementedError
    def search(self,lines,words):
        result_lines = []
        for line in lines:
            if self.lsearch_rule.search(line,words):
                result_lines.append(line)
        return result_lines

class LsSearch_notin(LinesSearchRule):
    def __init__(self):
        self.lsearch_rule = LSearch_notin()

class LsSearch_re(LinesSearchRule):
    def __init__(self):
        self.lsearch_rule = LSearch_re()

"""kmp搜索算法,用以测试系统可扩展性,2022-5-26"""
class LsSearch_kmp(LinesSearchRule):
    def __init__(self):
        self.lsearch_rule = LSearch_kmp()

#策略模式：查询规则上下文
class LinesSearchContext(object):
    def __init__(self,search_rule):
        self.search_rule = getattr(LinesSearchRule_Context,search_rule,None)()
        print("当前搜索算法：{}".format(search_rule))
    def search(self,lines,words):
        return self.search_rule.search(lines,words)