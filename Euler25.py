from math import *


class BigFib:

    def __init__(self):
        self.term = 3
        self.Gold = (1 + 5 ** 0.5) / 2
        self.gold = (1 - 5 ** .5) / 2
        self.factor = log(10) / log(self.Gold)
        # self.factor = round(self.factor, 1)
        print self.factor
        self.fibs = [1, 1]

    def nthFib(self, n):
        return (self.Gold ** n - self.gold ** n) / (5 ** .5) / 1E10

    def calcTerm(self):
        lastOne = 1
        lastTwo = 1
        nextTerm = 0
        while nextTerm < 5E10:
            nextTerm = lastOne + lastTwo
            lastTwo = lastOne
            lastOne = nextTerm
            self.fibs.append(nextTerm)
            print nextTerm, self.term, self.term / test.factor + 1
            self.term += 1

        return self.term

    def calcTerm2(self):
        n = 4700
        while self.nthFib(n) < 100:
            n += 1
        return n

test = BigFib()
test.calcTerm2()
print 999 * test.factor
print test.nthFib(50)