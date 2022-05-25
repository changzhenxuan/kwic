import re
class Line(object):
    def __init__(self,sentence):
        self.sentence = re.sub(r'[ ]+',' ',sentence.strip())

        self.words = self.get_words()
        self.word_num = self.get_wordnum()
        self.shift_sentences = []

    def get_words(self):
        return re.split(r'[ ]+',self.sentence)

    def get_wordnum(self):
        return len(self.words)
            
    def cyclicShift(self):
        for i in range(len(self.words)):
            shift_sentence = ' '.join(self.words[i+1:]+self.words[:i+1])
            self.shift_sentences.append(shift_sentence)