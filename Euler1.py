# If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9.
# The sum of these multiples is 23.
# Find the sum of all the multiples of 3 or 5 below 1000.

n = 0
threes = 0
fives = 0

while threes < 1000:	
    if fives < 1000:
        total += fives

    if threes % 5 == 0:
        pass
    else:
        total += threes

    n += 1
    threes = 3*n
    fives = 5*n

print total

