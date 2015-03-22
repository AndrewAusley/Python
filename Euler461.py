from math import *

class ApproxPi:

    def __init__(self, n):
        self.n = n
        self.precision = e**(1.0 / n) - 1
        self.max = round(log(pi + 1) * n)
        self.min = 0
        self.maxLevel = 0

    def calcPi(self):
        k1 = 0.0
        level = 2
        pin = round(pi*self.n)
        print "First order pi is:", pin
        while k1 < self.max:
            k2 = 0.0
            while k2 < self.max:
                k3 = 0.0
                while k3 < self.max:
                    k4 = pin - k1 - k2 - k3
                    if 0 < k4 < self.max:
                        arr = self.taylor(pin, level, k1, k2, k3, k4)
                        if arr[1] > level:
                            pin = arr[0]
                            level = arr[1]
                            k1 = 0.0
                            k2 = 0.0
                            k3 = 0.0
                    k3 += 1
                k2 += 1
            k1 += 1

    def taylor(self, pin, level, k1, k2, k3, k4):
        pit = pi*self.n
        sub = [0.0, pin]
        t = 2
        while t <= level:
            x = self.xi(t, k1, k2, k3, k4)
            pit -= sub[t-1]
            if x[0] == round(pit)*x[1]:
                sub.append(round(x[0]/x[1]))
                if t == level:
                    # probably annotate data points here
                    level += 1
                    x = self.xi(level, k1, k2, k3, k4)
                    return round(pi*self.n) - sum(sub[2:len(sub)]) - round(x[0]/x[1]), level
            else:
                if t == level:
                    level += 1
                    return round(pi*self.n) - sum(sub[2:len(sub)]) - round(x[0]/x[1]), level
                else:
                    return pin, level
            t += 1

    def xi(self, i, k1, k2, k3, k4):
        ord_num = k1**i + k2**i + k3**i + k4**i
        ord_den = factorial(i)*self.n**(i-1)
        return ord_num, ord_den


test = ApproxPi(20)
test.calcPi()
