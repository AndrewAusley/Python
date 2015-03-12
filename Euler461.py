

import math
import mpmath

class ApproxPi:

    def __init__(self):
        self.error = abs(math.e**(6.0/200)+ math.e**(75.0/200)+ math.e**(89.0/200)+ math.e**(226.0/200) - 4 - math.pi)
        print self.error
        self.index1 = 0
        self.index2 = 0
        self.index3 = 0
        self.index4 = 0

        self.block1 = []
        self.block2 = []
        self.block3 = []
        self.block4 = []
        for i in range(-25, 25):
            self.block1.append(math.e ** ((50 * 6.0 + i) / 10000))
            self.block2.append(math.e ** ((50 * 75.0 + i) / 10000))
            self.block3.append(math.e ** ((50 * 89.0 + i) / 10000))
            self.block4.append(math.e ** ((50 * 226.0 + i) / 10000))

    def minimizeError(self):
        for a in range(0, 50):
            for b in range(0, 50):
                for c in range(0, 50):
                    for d in range(0, 50):
                        error = abs(self.block1[a] + self.block2[b] + self.block3[c] + self.block4[d] - 4 - math.pi)
                        if error < self.error:
                            self.error = error
                            self.index1 = a
                            self.index2 = b
                            self.index3 = c
                            self.index4 = d
        self.convertIndices()

    def convertIndices(self):
        self.index1 = self.index1 + 6 * 50
        self.index2 = self.index2 + 75 * 50
        self.index3 = self.index3 + 89 * 50
        self.index4 = self.index4 + 226 * 50

test = ApproxPi()
test.minimizeError()
print 2*pi
print test.error, test.index1**2 + test.index2**2 + test.index3**2 + test.index4**2

