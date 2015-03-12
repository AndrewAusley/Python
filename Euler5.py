# 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

import Euler3


class MinimumMultiple:

    def __init__(self, upperLimit):
        self.primeFactor = Euler3.PrimeFactor()
        self.factors = range(1, upperLimit + 1, 1)

    def collapseFactors(self):
        index = -1
        while (len(self.factors) + index) > 0:
            index2 = index - 1
            while (len(self.factors) + index2) >= 0:
                if self.factors[index] % self.factors[index2] == 0:
                    del self.factors[index2]
                    continue
                else:
                    index2 -= 1
            index -= 1

    def generateMinimumMultiple(self):
        self.collapseFactors()
        minFactors = {self.primeFactor.primes[k]: 0 for k in range(0, len(self.primeFactor.primes))}
        for i in range(0, len(self.factors)):
            tempFactors = self.primeFactor.factor(self.factors[i])
            for j in range(0, len(tempFactors)):
                numFac = tempFactors.count(tempFactors[j])
                curCount = minFactors[tempFactors[j]]
                if numFac > curCount:
                    minFactors[tempFactors[j]] = numFac

        product = 1
        for x in self.primeFactor.primes:
            product *= x**minFactors[x]

        return product


test = MinimumMultiple(20)
print test.generateMinimumMultiple()