

class AmicableNums:

    def __init__(self, upperlimit):
        self.sums = {}
        self.upperlimit = upperlimit
        self.amicables = []

    def sumAmicables(self):

        for i in range(2, self.upperlimit + 1):
            if i in self.sums:
                continue
            else:
                temp1 = sum(self.generateFactors(i))
                self.sums[i] = temp1
                temp2 = sum(self.generateFactors(temp1))
                self.sums[temp1] = temp2
                if i == temp2 and i != temp1:
                    self.amicables.append(i)
                    self.amicables.append(temp1)
        return sum(self.amicables)

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

test = AmicableNums(10000)
print test.sumAmicables()
print test.amicables