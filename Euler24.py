# A permutation is an ordered arrangement of objects. For example, 3124 is one possible
# permutation of the digits 1, 2, 3 and 4. If all of the permutations are listed numerically
# or alphabetically, we call it lexicographic order. The lexicographic permutations of 0, 1 and 2 are:
#
# 012   021   102   120   201   210
#
# What is the millionth lexicographic permutation of the digits 0, 1, 2, 3, 4, 5, 6, 7, 8 and 9?

# n!/(n-k)! for k terms of n options

from math import *


class NthPermutation:

    def __init__(self, nth):
        self.n = 10
        self.ns = range(0, self.n)
        self.k = 10
        self.index = nth - 1
        self.perm = []
        self.nthperm = 0

    def calcPermutation(self):
        ind = self.index
        x = 1
        while x <= self.k:
            perms = factorial(self.k - x)
            nextDigit = ind / perms
            self.perm.append(self.ns[nextDigit])
            del self.ns[nextDigit]
            ind %= perms
            x += 1
        self.convInt()

    def convInt(self):
        total = 0
        for i in range(0, len(self.perm)):
            total *= 10
            total += self.perm[i]
        self.nthperm = total


    def nPr(self, n, k):
        return factorial(n)/factorial(n-k)

test = NthPermutation(1000000)
test.calcPermutation()
print test.nthperm
