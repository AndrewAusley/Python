# Find the sum of all prime number < 2,000,000

import Euler3


class PrimeSieve:

    def __init__(self, upperLimit):
        self.upperlimit = upperLimit
        self.sieve = range(0, self.upperlimit)
        self.sieve[1] = 0

    def runSieve(self):
        index = 0
        while index < len(self.sieve):
            if self.sieve[index] != 0:
                x = 2
                while self.sieve[index] * x < len(self.sieve):
                    self.sieve[self.sieve[index] * x] = 0
                    x = x + 1
            index = index + 1

    def cleanup(self):
        x = 0
        while x < len(self.sieve):
            if self.sieve[x] == 0:
                del self.sieve[x]
            else:
                x = x + 1

test = PrimeSieve(2000000)
test.runSieve()
print sum(test.sieve)

