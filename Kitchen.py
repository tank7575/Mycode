from sys import exit
from random import randint
from textwrap import dedent
import pdb
class room(object):
    pass

class Engine(object):

    def __init__(self, scene_map):
        self.scene_map = scene_map

    def play(self):
        current_scene = self.scene_map.opening_scene()
        last_scene = self.scene_map.next_scene('finished')

        while current_scene != last_scene:
            next_scene_name = current_scene.enter()
            current_scene = self.scene_map.next_scene(next_scene_name)

        current_scene.enter()

class Living_room(room):

    def enter(self):
        print("You wakes up from his nap and finds nobody in the house")
        print("You walks around the living room and does not know what to do")

        action = input(">  ")

class Kitchen(room):

    def enter(self):
        print("HI")


class Dining_room:
    pass
class Bathroom:
    pass
class Bed_room1:
    pass
class Bed_room2:
    pass
class Outside:
    pass
class Shop:
    pass
class Death:
    pass
class Finished:
    def enter(self):
        print("You won!!")
        return "finished"


class Map(object):

    room = {
    'living_room': Living_room(),
    'kitchen': Kitchen(),
#    "Dining_room": Dining_room(),
#    "Bathroom": Bathroom(),
#    "Bed_room1": Bed_room1(),
#    "Bed_room2": Bed_room2(),
#    "Outside": Outside(),
#    "Shop": Shop(),
     'death': Death(),
     'finished': Finished
    }

    def __init__(self, start_scene):
        self.start_scene = start_scene

    def next_scene(self, scene_name):
        val = Map.room.get(scene_name)
        return val

    def opening_scene(self):
        return self.next_scene(self.start_scene)


map = Map('living_room')
game = Engine(map)
game.play()
