

class FactorTriangle:

    def __init__(self, position):
        self.number = [0, 1, 3]
        self.position = position

    def factorTriangles(self):
        index = 3
        while True:
            self.number.append(self.number[-1] + index)
            index = index + 1
            factors = self.generateFactors(self.number[-1])
            factors.insert(0, 1)
            factors.append(self.number[-1])
            if len(factors) >= 500:
                return self.number[-1]

    def generateFactors(self, num):
        factors = []
        start = 2
        end = num / start
        while start < end:
            if num % start == 0:
                dividend = num / start
                factors.append(start)
                factors.append(dividend)
                end = dividend
            start = start + 1
        return factors

test = FactorTriangle(25)
print test.factorTriangles()