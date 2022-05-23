from LineSearchRule import LSearch_notin,LSearch_re
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

#策略模式：查询规则上下文
class LinesSearchContext(object):
    def __init__(self,search_rule_num=0):
        if search_rule_num == 0:
            self.search_rule = LsSearch_notin()
        elif search_rule_num == 1:
            self.search_rule = LsSearch_re()
    def search(self,lines,words):
        return self.search_rule.search(lines,words)