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