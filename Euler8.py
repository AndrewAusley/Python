# The four adjacent digits in the 1000-digit number that have the greatest product are 9 x 9 x 8 x 9 = 5832.
# Find the thirteen adjacent digits in the 1000-digit number that have the greatest product.
# What is the value of this product?

class NumberWindow:

    number = "7316717653133062491922511967442657474235534919493496983520312774506326239578318016" \
             "98480186947885184385861560789112949495459501737958331952853208805511125406987471585" \
             "23863050715693290963295227443043557668966489504452445231617318564030987111217223831" \
             "13622298934233803081353362766142828064444866452387493035890729629049156044077239071" \
             "38105158593079608667017242712188399879790879227492190169972088809377665727333001053" \
             "36788122023542180975125454059475224352584907711670556013604839586446706324415722155" \
             "39753697817977846174064955149290862569321978468622482839722413756570560574902614079" \
             "72968652414535100474821663704844031998900088952434506585412275886668811642717147992" \
             "44429282308634656748139191231628245861786645835912456652947654568284891288314260769" \
             "00422421902267105562632111110937054421750694165896040807198403850962455444362981230" \
             "98787992724428490918884580156166097919133875499200524063689912560717606058861164671" \
             "09405077541002256983155200055935729725716362695618826704282524836008232575304207529" \
             "63450"

    def __init__(self, window):
        self.number = self.number.split('0')
        self.window = window
        self.max = 0
        self.product = 0

    def separateByZeros(self):
        x = 0
        while x < len(self.number):
            if len(self.number[x]) < self.window:
                del(self.number[x])
            else:
                self.findWindow(self.number[x])
                x += 1

    def findWindow(self, test):
        # Computer initial product
        testprod = 1
        for x in range(0, self.window):
            testprod *= int(test[x])
        if testprod > self.product:
            self.product = testprod
            self.max = test[0:self.window]

        # Iterate using one * and one /
        i = self.window
        while i < len(test):
            testprod = testprod / int(test[i - self.window])
            testprod *= int(test[i])
            if testprod > self.product:
                self.product = testprod
                self.max = test[i - self.window + 1:i + 1]

            i = i + 1


test = NumberWindow(13)
test.separateByZeros()
print test.max, test.product