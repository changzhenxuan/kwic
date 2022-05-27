from Package.KwicClass import LinesSortRule_Context

class LinesSortRule(object):
    def __init__(self):
        raise NotImplementedError
    def cmp(self):
        pass

class SpaceAdvance(LinesSortRule):
    def __init__(self):
        #初始化字符优先表
        self.order = [' ']
        for i in range(26):
            ch = chr(ord('a')+i)
            self.order.append(ch)
            self.order.append(ch.upper())

    def cmp(self,line1,line2):
        #正排序，小的在前
        #空格优先 => 当line2=line1+xxx时，line1优先
        s1,s2 = line1.sentence,line2.sentence
        if s1 == '': return 1
        if s2 == '': return -1
        n = min(len(s1), len(s2))
        for i in range(n):
            if s1[i] == s2[i]:continue
            else:
                return self.order.index(s1[i]) - self.order.index(s2[i])
        return len(s1)-len(s2)

class LinesSortContext(object):
    def __init__(self,sort_rule):
        self.sort_rule = getattr(LinesSortRule_Context,sort_rule,None)()
        print("当前排序算法：{}".format(sort_rule))
    def getCmp(self):
        return self.sort_rule.cmp