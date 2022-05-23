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
        n = min(len(line1), len(line2))
        for i in range(n):
            if line1[i] == line2[i]:continue
            else:
                return self.order.index(line1[i]) - self.order.index(line2[i])
        return len(line1)-len(line2)