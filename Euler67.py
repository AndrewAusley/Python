# By starting at the top of the triangle below and moving to adjacent numbers on the row below, the maximum total from top to bottom is 23.
#
# 3
# 7 4
# 2 4 6
# 8 5 9 3
#
# That is, 3 + 7 + 4 + 9 = 23.
#
# Find the maximum total from top to bottom of the triangle below:


class PyramidPath:

    def __init__(self, levels):
        self.max = [0]
        self.levels = levels
        self.pyr = []
        f = open('p067_triangle.txt', 'r')
        for line in f:
            line = line.strip().split()
            line = map(int, line)
            self.pyr.append(line)

    def calcPathCost(self):
        paths = self.pyr[:][:]
        row = self.levels - 2
        while row >= 0:
            col = 0
            print len(paths[row])
            while col < len(paths[row]):

                if paths[row + 1][col] > paths[row + 1][col + 1]:
                    paths[row][col] += paths[row + 1][col]
                else:
                    paths[row][col] += paths[row + 1][col + 1]
                col += 1
            row -= 1
        return paths[0][0]

test = PyramidPath(100)
print test.calcPathCost()
