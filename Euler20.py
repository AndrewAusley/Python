import math


class SumFactDigits:

    def __init__(self, num):
        self.number = math.factorial(num)
        self.sum = 0

    def sumDigits(self):
        num = str(self.number)
        for i in range(0, len(num)):
            self.sum += int(num[i])
        return self.sum

test = SumFactDigits(100)
print test.sumDigits()