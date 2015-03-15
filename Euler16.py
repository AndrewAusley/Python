

class SumDigits:

    def __init__(self, powerOfTwo):
        self.num = 2**powerOfTwo

    def calcSum(self):
        s = 0
        while self.num:
            s += self.num % 10
            self.num /= 10
        return s

test = SumDigits(1000)
print test.calcSum()



