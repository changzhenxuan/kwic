from functools import cmp_to_key
import re
#Line
class Line(object):
    def __init__(self,sentence):
        self.sentence = sentence

        self.words = self.get_words()
        self.word_num = self.get_wordnum()
        self.shift_sentences = []

    def get_words(self):
        return self.sentence.split(' ')

    def get_wordnum(self):
        return len(self.words)
            
    def cyclicShift(self):
        for i in range(len(self.words)):
            shift_sentence = ' '.join(self.words[i+1,:]+self.words[:i+1])
            self.shift_sentences.append(shift_sentence)

#python 自定义比较规则，见https://blog.csdn.net/HappyRocking/article/details/106648245
"""
def cmp(t1, t2):
    "比较函数，需要满足：t1>t2则返回正数，t1=t0则返回0，t1<t2则返回负数。"
    if t1.x == t2.x:
        return t1.y - t2.y
    return t1.x - t2.x

# 新建cmp函数    
l2 = sorted(l, key=cmp_to_key(cmp))
print_list(l2)
"""
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

class LinesSearchContext(object):
    def __init__(self,search_rule_num=0):
        if search_rule_num == 0:
            self.search_rule = LsSearch_notin()
        elif search_rule_num == 1:
            self.search_rule = LsSearch_re()
    def search(self,lines,words):
        return self.search_rule.search(lines,words)
            

class LineSearchRule(object):
    def __init__(self):
        raise NotImplementedError
    def search(self):
        pass

class LSearch_notin(LineSearchRule):
    def __init__(self):
        pass
    def search(self,line,words):
        for word in words:
            if word not in line.words:
                return False
        return True

class LSearch_re(LineSearchRule):
    def __init__(self):
        pass
    def search(self,line,words):
        for word in words:
            if re.search(word,line.sentence)==None:
                return False
        return True


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
