import re
class LineSearchRule(object):
    def __init__(self):
        raise NotImplementedError
    def search(self):
        pass

class LSearch_notin(LineSearchRule):
    def __init__(self):
        pass
    def search(self,line,keywords):
        for word in keywords:
            if word not in line.words:
                return False
        return True

class LSearch_re(LineSearchRule):
    def __init__(self):
        pass
    def search(self,line,keywords):
        for word in keywords:
            if re.search(word,line.sentence)==None:
                return False
        return True

"""kmp搜索算法,用以测试系统可扩展性,2022-5-26"""
class LSearch_kmp(LineSearchRule):
    def __init__(self):
        pass
    def search(self,line,keywords):
        for word in keywords:
            if self.kmp(line.sentence,word)==0:
                return False
        return True

    def same_start_end(self,s):
        """最长前后缀相同的字符位数"""
        n = len(s) #整个字符串长度
        j = 0 # 前缀匹配指向
        i = 1 # 后缀匹配指向
        result_list=[0]*n
        while i < n:
            if j == 0 and s[j] != s[i]:  #　比较不相等并且此时比较的已经是第一个字符了
                result_list[i] = 0    # 值为０
                i += 1  # 向后移动
            elif s[j] != s[i] and j != 0: #比较不相等,将j值设置为ｊ前一位的result_list中的值，为了在之前匹配到的子串中找到最长相同前后缀
                j = result_list[j-1]
            elif s[j] == s[i]:   #相等则继续比较
                result_list[i] = j+1
                j = j+1
                i = i+1
        return result_list

    def kmp(self,s,p):
        """kmp算法,s是字符串,p是模式字符串,若有一个匹配到,返回1,没匹配到返回0"""
        s_length = len(s)
        p_length = len(p)
        i = 0  # 指向s
        j = 0  # 指向p
        next = self.same_start_end(p)
        while i < s_length:
            if s[i] == p[j]:  # 对应字符相同
                i += 1
                j += 1
                if j >= p_length:  # 完全匹配
                    return 1
            elif s[i] != p[j]:  # 不相同
                if j == 0:    # 与模式比较的是模式的第一个字符
                    i += 1
                else:        # 取模式当前字符之前最长相同前后缀的前缀的后一个字符继续比较
                    j = next[j]
        if i == s_length:    # 没有找到完全匹配的子串
            return 0