from math import *


class BigFib:

    def __init__(self):
        self.term = 3
        self.gold = (1 + 5 ** 0.5) / 2
        self.factor = log(10) / log(self.gold)
#        self.factor = round(self.factor, 1)
        print self.factor
        self.fibs = [1, 1]

    def calcViaRation(self):
        x = 50
        while self.gold**x < 1E1000:
            x += 1
        return x

    def calcTerm(self):
        lastOne = 1
        lastTwo = 1
        nextTerm = 0
        while nextTerm < 1E100:
            nextTerm = lastOne + lastTwo
            lastTwo = lastOne
            lastOne = nextTerm
            self.fibs.append(nextTerm)
            print nextTerm, self.term, self.term / test.factor + 1
            self.term += 1

        return self.term

test = BigFib()
test.calcTerm()
print 999 * test.factor
print test.factor