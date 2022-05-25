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