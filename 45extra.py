from sys import exit
from random import randint

class Scene(object):
    def enter(self):
        pass


class Engine(object):
    def __init__(self, scene_map):
        print ("Engine __init__ has scene map", scene_map)
        self.scene_map = scene_map

    def play(self):
        current_scene = self.scene_map.opening_scene()
        print ("Plays first scene", current_scene)

        while True:
            print ("\n------------")
            next_scene_name = current_scene.enter()
            print ("next scene", next_scene_name)
            current_scene = self.scene_map.next_scene(next_scene_name)

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
    pass

class Bridge(Scene):
    pass

class EscapePod(Scene):
     pass

class Death(Scene):
    pass

class Map(object):
    scenes = {
        'central_corridor' : CentralCorridor(),
        'laserweaponarmory' : LaserWeaponArmory(),
        'Bridge' : Bridge(),
        'escape_pod' : EscapePod(),
        'Death' : Death()
    }
    def __init__(self, start_scene):
        self.start_scene = start_scene
        print ("start_scene in __init__", self.start_scene)

    def next_scene(self, scene_name):
        print ("start_scene in next_scene")
        val = Map.scenes.get(scene_name)
        print ("next_scene returns", val)
        return val

    def opening_scene(self):
        print ("start_scene in opening_scene")
        return self.next_scene(self.start_scene)

a_map = Map('central_corridor')
a_game = Engine(a_map)
a_game.play()
