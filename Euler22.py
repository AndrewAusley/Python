# Using names.txt (right click and 'Save Link/Target As...'), a 46K text file containing over five-thousand first names,
# begin by sorting it into alphabetical order. Then working out the alphabetical value for each name, multiply this
# value by its alphabetical position in the list to obtain a name score.
#
# For example, when the list is sorted into alphabetical order, COLIN, which is worth
# 3 + 15 + 12 + 9 + 14 = 53, is the 938th name in the list. So, COLIN would obtain a score of 938 x 53 = 49714.
#
# What is the total of all the name scores in the file?


class NameScore:

    def __init__(self):
        f = open('p022_names.txt', 'r')
        self.names = f.read().split(",")
        self.names.sort()
        self.sum = 0

    def calcScore(self):
        for i in range(0, len(self.names)):
            temp = 0
            for j in range(0, len(self.names[i])):
                temp += ord(self.names[i][j]) - 64
            self.sum += temp*(i + 1)


test = NameScore()
test.calcScore()
print test.sum