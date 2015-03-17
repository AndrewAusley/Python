# You are given the following information, but you may prefer to do some research for yourself.
#
# 1 Jan 1900 was a Monday.
# Thirty days has September,
# April, June and November.
# All the rest have thirty-one,
# Saving February alone,
# Which has twenty-eight, rain or shine.
# And on leap years, twenty-nine.
# A leap year occurs on any year evenly divisible by 4, but not on a century unless it is divisible by 400.
# How many Sundays fell on the first of the month during the twentieth century (1 Jan 1901 to 31 Dec 2000)?


class SundayCounter:

    def __init__(self):
        self.day = 2
        self.year = 1901
        self.months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        self.sundays = 0

    def calcSundays(self):
        for y in range(1901, 2001):
            for m in range(0, 12):
                if self.day % 7 == 0:
                    self.sundays += 1
                if m == 1 and y % 4 == 0:
                    self.day += 1
                self.day += self.months[m]

test = SundayCounter()
test.calcSundays()
print test.sundays
