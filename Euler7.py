# By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

# What is the 10 001st prime number?

import Euler3


class findXPrime:

	def __init__(self):
		self.pf = Euler3.PrimeFactor()

	def findPrime(self, x):
		num = x
		if num < len(self.pf.primes):
			return self.pf.primes[num - 1]
		else:
			while len(self.pf.primes) < num:
				self.pf.generateNextPrime()

			return self.pf.primes[num - 1]


test = findXPrime()
print test.findPrime(10001)
# 104743