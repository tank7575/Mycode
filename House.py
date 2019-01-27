#from Living_room import *

class House(object):

    def __init__(self, name):
        self.name = name

    def door(self):
        print(self.name + " " + "opens the door and goes into the living room ")
        print(self.name + " " + "and find that the house is empty")

    def Chair(self):
        print(self.name + " " + "sit in the chair and takes a nap")

class Living_room(object):

    def __init__(self,name):
        self.name = name

    def tv(self):
        print(self.name + " " + "turn on the Tv to see if anything is on")
        print(self.name + " " + "filp throught the channels and find a football game on.")



def main():
    dad = House("Dad")
    dad.door()
    dad.Chair()
    dad = Living_room("Dad")
    dad.tv()

if __name__ == "__main__":
        main()
