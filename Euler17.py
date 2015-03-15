# If the numbers 1 to 5 are written out in words: one, two, three, four, five,
# then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.

# If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words, how many letters would be used?

# NOTE: Do not count spaces or hyphens. For example, 342 (three hundred and forty-two) contains 23 letters and
# 115 (one hundred and fifteen) contains 20 letters. The use of "and" when writing out numbers is in compliance
# with British usage.

class SumNumberLetters:

    def __init__(self, upperlimit):
        self.upperlimit = upperlimit
        self.nums = {1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five', 6: 'six', 7: 'seven', 8: 'eight', 9: 'nine',
                    10: 'ten', 11: 'eleven', 12: 'twelve', 13: 'thirteen', 14: 'fourteen', 15: 'fifteen', 16: 'sixteen',
                    17: 'seventeen', 18: 'eighteen', 19: 'nineteen', 20: 'twenty', 30: 'thirty', 40: 'forty',
                    50: 'fifty', 60: 'sixty', 70: 'seventy', 80: 'eighty', 90: 'ninety', 100: 'onehundred',
                    200: 'twohundred', 300: 'threehundred', 400: 'fourhundred', 500: 'fivehundred', 600: 'sixhundred',
                    700: 'sevenhundred', 800: 'eighthundred', 900: 'ninehundred', 1000: 'onethousand'}

        self.total = ''

    def calcLength(self):
        for i in range(1, self.upperlimit + 1):
            if i in self.nums:
                self.total += self.nums[i]
            else:
                self.buildString(i)

    def buildString(self, i):
        hundreds = ''
        tens = ''
        ones = ''
        temp1 = 0
        temp2 = 0
        if (i % 100) in self.nums:
            tens = self.nums[i % 100]
            temp2 = i % 100
        else:
            temp1 = i % 10
            if temp1 != 0:
                ones = self.nums[temp1]
            else:
                ones = ''
            temp2 = (i - temp1) % 100
            if temp2 != 0:
                tens = self.nums[temp2]
            else:
                tens = ''

        if i > 100:
            hundreds = self.nums[i - temp1 - temp2] + 'and'
            self.total += hundreds

        self.total += tens
        self.total += ones


test = SumNumberLetters(1000)
test.calcLength()
print len(test.total), test.total