class Scene(object): pass

class CentralCorridor(Scene):
    def enter(self): 
        input("Central Corridor. >")
        return 'finished'

class Finished(Scene):
    def enter(self): 
        print("You won! Good job.")
        return 'finished'

class Engine(object):
    # make an instance attribute named 'scene_map'
    # for scene map you have to set an instance of class Map() with a scene subclass as argument
    # e.g. Map('central_corridor')
    def __init__(self, scene_map):
        self.scene_map = scene_map
        print("Line 21: ", repr(self.scene_map))

    # make a method named 'play'
    def play(self):
        # set 'current_scene' to the following: from class Map call the method/function 'opening_scene'
        current_scene = self.scene_map.opening_scene()
        print("Line 26: ", repr(current_scene))
        # set 'last_scene' to the following: from class Map call the method/function
        # 'next_scene' with argument 'finished'
        last_scene = self.scene_map.next_scene('finished')
        print("Line 30: ", repr(last_scene))

        # run this as long as current_scene aren't the same
        while current_scene != last_scene:
            # set 'next_scene_name' to the following: call the method 'opening_scene' from
            # class Map. Method 'opening_scene' calls from the current scene (class) the method 'enter'
            # the return value of the 'enter' method is a scene name.
            next_scene_name = current_scene.enter()
            print("Line 38: ", repr(next_scene_name))
            # set 'current_scene' to the following: from class Map call the method 'next_scene' with
            # the return value of the 'enter' method of a scene subclass.
            current_scene = self.scene_map.next_scene(next_scene_name)
            print("Line 42: ", repr(current_scene))

        # run after the while loop is over
        # from 'current_scene' call the method 'enter'
        # program finishes
        current_scene.enter()
        print("Line 48: ", repr(current_scene.enter()))


class Map(object):
    # make a dictionary as a class attribute with the scene subclasses as value
    scenes = {
            'central_corridor': CentralCorridor(),
            'finished': Finished(),
    }
    
    # make an instance attribute named 'start_scene'
    # set as parameter a key-name from the class attribute dictionary scenes
    def __init__(self, start_scene):
        self.start_scene = start_scene

    # make a method called 'next_scene' with a parameter 'scene_name'
    def next_scene(self, scene_name):
        # set 'val' to the following: from class Map get from class attribute dictionary
        # 'scenes' the key speficied in the parameter of the function
        val = Map.scenes.get(scene_name)
        print("Line 68: ", repr(val))
        # return the scene subclass called in 'val'
        return val

    # make a method called 'opening_scene' with parameter 'self'
    def opening_scene(self):
        # return the method next_scene from map with parameter 'start_scene'
        print("Line 75: ", repr(self.next_scene(self.start_scene)))
        return self.next_scene(self.start_scene)


# set 'a_map' to an instance of class Map with the instance attribute 'central_corridor'
a_map = Map('central_corridor')
print("Line 81: ", repr(a_map))
# set 'a_game' to an instance of class Engine with class Map with the instance attribute 'central_corridor' as instance attribute
a_game = Engine(a_map)
print("Line 84: ", repr(a_game))
# from 'a_game' call the method play()
# or
# from class Engine call the method play()
a_game.play()
print("Line 89: ", repr(a_game.play()))