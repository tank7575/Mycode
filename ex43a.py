from sys import exit
from random import randint
from textwrap import dedent

class Scene(object):

    def enter(self):
        pass

class Engine(object):

    def __init__(self, scene_map):
        print ("Engine __init__ has scene map", scene_map)
        self.scene_map = scene_map

    def play(self):
        print(">>> play3")
        current_scene = self.scene_map.opening_scene()
        print ("Plays first scene", current_scene)
        last_scene = self.scene_map.next_scene('finished')
        print("^^^ before while current_scene4=", current_scene, "last_scene5=", last_scene)
        while current_scene != last_scene:
            print("^top of while current_scene6=",current_scene, "last_scene7=", last_scene)
            next_scene_name = current_scene.enter()
            current_scene = self.scene_map.next_scene(next_scene_name)
            print("^ end of while current_scene8=", current_scene, "last_scene9",
                 last_scene, "next_scene_name11", next_scene_name)

            print ("<<< end of play: current_scene12=", current_scene)

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
        print("You do a dive roll into the Weapon Armory, crouch and scan the room")
        print("for more Gothons that might be hiding.  It's dead quiet, too quiet.")
        print("You stand up and run to the far side of the room and find the")
        print("neutron bomb in its container.  There's a keypad lock on the box")
        print("and you need the code to get the bomb out.  If you get the code")
        print("wrong 10 times then the lock closes forever and you can't")
        print("get the bomb.  The code is 3 digits.")
        code = "%d%d%d" % (randint(1,9), randint(1,9), randint(1,9))
        guess = input("[keypad]> ")
        guesses = 0

        while guess != code and guesses < 10:
            print("BZZZZEDDD!")
            guesses += 1
            guess = input("[keypad]> ")

        if guess == code:
            print("The container clicks open and the seal breaks, letting gas out.")
            print("You grab the neutron bomb and run as fast as you can to the")
            print("bridge where you must place it in the right spot.")
            return 'the_bridge'
        else:
            print("The lock buzzes one last time and then you hear a sickening")
            print("melting sound as the mechanism is fused together.")
            print("You decide to sit there, and finally the Gothons blow up the")
            print("ship from their ship and you die.")
            return 'death'

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

    scenes = {
    'central_corridor': CentralCorridor(),
    'laser_weapon_armory': LaserWeaponArmory(),
    #'the_bridge': TheBridge(),
    #'escape_pod': EscapePod(),
    'death': Death(),
    #'finished': Finished(),
    }

    def __init__(self, start_scene):
        self.start_scene = start_scene
        print ("start_scene in __init__", self.start_scene)

    def next_scene(self, scene_name):
        print(">>> next_scene2=")
        val = Map.scenes.get(scene_name)
        print ("next_scene returns", val)
        return val

    def opening_scene(self):
        print(">>> opening_scene1=")
        print ("start_scene in opening_scene")
        return self.next_scene(self.start_scene)



a_map = Map('central_corridor')
a_game = Engine(a_map)
a_game.play()
