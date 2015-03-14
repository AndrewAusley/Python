# Calculate number of paths through 20x20 square
import math


class LatticePath:

    def __init__(self):
        self.paths = 0

    def calcPaths(self, squares):
        return self.nCr(2*squares, squares)

    def nCr(self, n, r):
        f = math.factorial
        return f(n) / f(r) / f(n-r)

test = LatticePath()
print test.calcPaths(20)
