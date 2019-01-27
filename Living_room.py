from House import *

class Living_room(House):

    def doors(self, name):
        print(self.name + " " + "wakes up from his nap and finds nobody in the house")
        print(self.name + " " + "walks around the living room and does not know what to do")



class Living_room(House):

    def __init__(self, name):
            self.name = name


    def doors(self, name):
        print(self.name + " " + "wakes up from his nap and finds nobody in the house")
        print(self.name + " " + "walks around the living room and does not know what to do")





room = {
        "Living_room": Living_room(),
        "Kitchen": Kitchen(),
        "Dining_room": Dining_room(),
        "Bathroom": Bathroom(),
        "Bed_room1": Bed_room1(),
        "Bed_room2": Bed_room2(),
        "Outside": Outside(),
        "Shop": Shop()
        }
