from sys import exit
from random import randint
from textwrap import dedent

class Scene(object):

    def enter(self):
        print("This scene is not yet configured. Subclass it and implement enter().")
        exit(1)

class Engine(object):

    def __init__(self, scene_map):
        self.scene_map = scene_map

    def play(self):

        current_scene = self.scene_map.startupgame()
        last_scene = self.scene_map.nextgame('finished')

        while current_scene != last_scene:

            next_scene_name = current_scene.enter()
            current_scene = self.scene_map.nextgame(next_scene_name)

        current_scene.enter()

class CentralCorridor(Scene):

    def enter(self):
        print("HI")

        action = input("> ")

        if action == "shoot":
            print("dead.")
            return 'death'

        elif action == "dodge":
            print("dodge.")
            return 'death'

        elif action == "tell a joke":
            print("joke.")
            return 'laser_weapon_armory'

        else:
            print("DOES NOT COMPUTE!")
            return 'central_corridor'

class LaserWeaponArmory(Scene):

    def enter(self):
        print("HeLLO World")

class TheBridge(Scene):

    def enter(self):
        pass

class EscapePod(Scene):

    def enter(self):
        pass

class Death(Scene):

    quips = [
        "You died.  You kinda suck at this.",
         "Your mom would be proud...if she were smarter.",
         "Such a luser.",
         "I have a small puppy that's better at this."
    ]

    def enter(self):
        print(Death.quips[randint(0, len(self.quips)-1)])
        exit(1)

class Finished(Scene):

    def enter(self):
        print("You won! Good job.")
        return "finished"



class Map(object):

    place = {
    'central_corridor': CentralCorridor(),
    #'laser_weapon_armory': LaserWeaponArmory(),
    #'the_bridge': TheBridge(),
    #'escape_pod': EscapePod(),
    'death': Death(),
    #'finished': Finished(),
    }
#  opengame  = start_scene
#  next_scene = opengame
#  opening_scene = startupgame
#  scene_name = location
# scens =  place
    def __init__(self, opengame):
        self.opengame = opengame

    def nextgame(self, location):
        val = Map.place.get(location)
        return val

    def startupgame(self):
        return self.nextgame(self.opengame)



map = Map('central_corridor')
game = Engine(map)
game.play()
