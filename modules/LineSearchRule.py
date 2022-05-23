#策略模式：查询策略/规则
class LineSearchRule(object):
    def __init__(self):
        raise NotImplementedError
    def search(self):
        pass

class LSearch_1(LineSearchRule):
    def __init__(self):
        pass
    def search(self,lines,words):
        result_lines = []
        for line in lines:
            flag = 1
            for word in words:
                if word not in line.words():
                    flag = 0
                    break
            if flag == 1:
                result_lines.append(line)
        return result_lines

#策略模式：查询规则上下文
class LineSearchContext(object):
    def __init__(self,search_rule_num):
        if search_rule_num == 1:
            self.search_rule = LSearch_1()
        else:
            pass
    def search(self,lines,words):
        return self.search_rule.search(lines,words)