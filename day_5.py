class Mama(object):
    def __int__(self):
        self.s = ' '
    def getStrings(self):
        self.s = input('Give me a string...')
    def printString(self):
        print(self.s.upper())

x = Mama()
print(x)

x.getStrings()
x.printString()
