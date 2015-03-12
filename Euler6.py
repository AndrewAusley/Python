# The sum of the squares of the first ten natural numbers is,
#
# 1^2 + 2^2 + ... + 10^2 = 385
# The square of the sum of the first ten natural numbers is,
#
# (1 + 2 + ... + 10)^2 = 55^2 = 3025
# Hence the difference between the sum of the squares of the first ten
# natural numbers and the square of the sum is 3025 - 385 = 2640.
#
# Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.


class SumOfCrossTerms:

	def __init__(self, upperLimit):
		self.m = upperLimit

	def sum(self):
		result = (self.m*(self.m + 1)/2)**2 - self.m*(self.m + 1)*(2*self.m + 1)/6
		return result

test = SumOfCrossTerms(100)
print test.sum()