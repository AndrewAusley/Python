# A palindromic number reads the same both ways.
# The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 x 99.
# Find the largest palindrome made from the product of two 3-digit numbers.


class PalindromeByFactors:

    def findPalindrome(self):
        for A in range(9, -1, -1):
            for B in range(9, -1, -1):
                for C in range(9, -1, -1):
                    pal = A*10**5 + B*10**4 + C*10**3 + C*10**2 + B*10 + A
                    factors = self.factor(pal)
                    if factors:
                        return pal, factors
                    else:
                        continue

    def factor(self, number):  # Find two three digit factors by brute force
        fac1 = 999

        while fac1 > 99:
            if number % fac1 == 0:
                fac2 = number / fac1
                if 99 < fac2 < 1000:
                    return fac1, fac2

            fac1 -= 1

        return False

test = PalindromeByFactors()
print test.findPalindrome()