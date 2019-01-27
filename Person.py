class Person:


    """A base class to define Person properties"""

    def __init__(self, name):
        print("^^^ name")
        self.name = name

    def speak(self, msg = '(Calling The Base Class)'):
                print("^^^ speak")
                print(self.name, msg)
