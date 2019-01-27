from Person import *
    #'''A derived clas to defing Hombre properties.'''

class Hombre(Person):
    print("<<<<< Hombre")
    def speak(self, msg):
        print(self.name, ':\n\tHola!', msg)
