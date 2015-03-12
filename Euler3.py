# The prime factors of 13195 are 5, 7, 13 and 29.
# What is the largest prime factor of the number 600851475143 ?

# There are two parts to this problem: factoring and finding primes.
# I'm seeding this with the primes I know off the top of my head to speed things up.
# This can be reduced to only 2 and it will be rebuilt


class PrimeFactor:

    def __init__(self):
        self.primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]

    def factor(self, number):
        factors = []
        seed = self.primes[:]
        while len(seed) > 0:
            if number % seed[0] == 0:
                result = number / seed[0]
                if result == 1:
                    factors.append(seed[0])
                    return factors
                else:
                    factors.append(seed[0])
                    factors = self.arrayMerge(factors, self.factor(result))
                    return factors
            else:
                if len(seed) != 1:
                    del seed[0]
                else:
                    seed.append(self.generateNextPrime())

    def generateNextPrime(self):
        index = 0
        candidate = self.primes[-1] + 2
        while index < len(self.primes):
            if candidate % self.primes[index] == 0 and self.primes[index]**2 <= candidate:
                candidate += 2
                index = 0
                continue
            else:
                index += 1

        self.primes.append(candidate)
        return candidate

    def arrayMerge(self, one, two):
        merged = one[:]
        if hasattr(two, "__len__"):
            for i in range(0, len(two)):
                merged.append(two[i])
        else:
            merged.append(two)

        return merged

