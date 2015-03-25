from math import *


class BigFib:

    def __init__(self):
        self.term = 3
        self.Gold = (1 + 5 ** 0.5) / 2
        self.gold = (1 - 5 ** .5) / 2
        self.factor = log(10) / log(self.Gold)
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

test = BigFib()
print ceil(999 * test.factor) + 1 