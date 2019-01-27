from Person import *


    #'''A derived class to define Man property'''

class Man(Person):
    print(">>>> Man")
    def speak(self, msg):
        print(self.name, ':\n\tHello!', msg)
