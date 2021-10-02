#!/usr/bin/env python 
import sys
import fileinput
import nltk
from nltk.tokenize import RegexpTokenizer
from collections import Counter

nltk.download('punkt')
tokenizer = nltk.RegexpTokenizer(r"\w+[’']\w+|\w+")

def tokenize(line): 
    return tokenizer.tokenize(line.lower())

class NgramCounter: 
    def __init__(self, n):
        self.n = n
        self.previous_words = []
        self.count = dict() 

    def process_word(self, word):
        # if word == 's':
            # print(line)
        if len(self.previous_words) == self.n - 1:
            phrase = " ".join(self.previous_words) + " " + word
            if phrase in self.count:
                self.count[phrase] += 1
            else:
                self.count[phrase] = 1
        self.previous_words.append(word)
        if len(self.previous_words) == self.n:
            self.previous_words = self.previous_words[1:]

    def top(self, top):
        c = Counter(self.count)
        return c.most_common(top)

    def report(self, topNumber=100): 
        c = Counter(self.count)
        for t in self.top(topNumber):
            print(t[1], " - " + t[0])
        print("In memory array size ", len(self.count))

if __name__ == '__main__':    
    counter = NgramCounter(3)
    for line in fileinput.input(sys.argv[1:]):
        for word in tokenize(line):
            counter.process_word(word)

    counter.report(100)
