# The following iterative sequence is defined for the set of positive integers:
# 
# n -> n/2 (n is even)
# n -> 3n + 1 (n is odd)
# 
# Using the rule above and starting with 13, we generate the following sequence:
# 
# 13 -> 40 -> 20 -> 10 -> 5 -> 16 -> 8 -> 4 -> 2 -> 1
# It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms.
# Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.
# 
# Which starting number, under one million, produces the longest chain?
# 
# NOTE: Once the chain starts the terms are allowed to go above one million.

import Euler3


class Collatz:

    def __init__(self):
        self.max = 0
        self.number = 0
        self.lengths = {}

    def calcChain(self, n):
        temp = [n]
        while n > 1:
            if n % 2 == 0:
                n /= 2
            else:
                n = 3 * n + 1
            if n in self.lengths:
                self.populateLengths(temp, n)
                return
            else:
                temp.append(n)

        self.populateLengths(temp, 1)


    def populateLengths(self, nums, n):
        total = len(nums)
        if n != 1:
            for i in range(0, total):
                self.lengths[nums[i]] = len(nums) - i + self.lengths[n]
        else:
            for i in range(0, total):
                self.lengths[nums[i]] = len(nums) - i


    def bruteTest(self, n):
        temp = []
        for x in range(0, n):
            temp = self.calcChain(x)
            if len(temp) > self.max:
                self.max = len(temp)
                self.number = x

test = Collatz()
test.calcChain(10)
print test.lengths
