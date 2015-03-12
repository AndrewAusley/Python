# a < b < c
# a**2 + b**2 = c**2
# a + b + c = 1000
# find a*b*c

import math
amax = 332
amin = 1

for a in range(1, 500):
    b = 1000 * (500 - a) / (1000 - a)
    c = math.sqrt(a**2 + b**2)
    if a+b+c == 1000 and a < b < c:
        print a,b,c, a*b*c
