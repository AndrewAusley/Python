
class NonabundantSums:

    def __init__(self):
        self.abundants = []
        self.nums = range(0, 28124)

    def calcAbundants(self):
        for i in range(12, 28124):
            if sum(self.generateFactors(i)) > i:
                self.abundants.append(i)

    def trashAbundantSums(self):
        i = 0
        length = len(self.abundants)
        while i < length:
            j = i
            while j < length:
                total = self.abundants[i] + self.abundants[j]
                if total < len(self.nums):
                    self.nums[total] = 0
                else:
                    break
                j += 1
            i += 1

    def calcSum(self):
        self.calcAbundants()
        self.trashAbundantSums()
        print sum(self.nums)

    def generateFactors(self, num):
        factors = [1]
        start = 2
        end = num / start
        while start < end:
            if num % start == 0:
                dividend = num / start
                factors.append(start)
                if start != dividend:
                    factors.append(dividend)
                end = dividend
            start += 1
        return factors

test = NonabundantSums()
test.calcSum()