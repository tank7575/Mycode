backpack = ["rope", "knive", "compass", "water bottle", "watch",
            "clothes", "shoes", "tent", "gloves"]

rules_for_hiking_in_woods = ['stay on path',
                            'drink plenty of water',
                            'don\'t feed animail',
                            'don\'t litter',
                            'do pick up trash']
people_to_hike_with = {"Luke": "LT",
                        "Lori": "LAT",
                        "Bill": "BC",
                        "Jon": "JS",
                        "Lonnie": "LA",
                        "John": "JD"
                        }

Trees_in_forest = {"pine": "pn",
                    "oak": "O",
                    "maple": "MA",
                    "ELM": "E",
                    "poplar": "PO",
                    "Sycamore": "SY",
                    "cottonwood": "CO"
                    }

def deep_woods():
    print("You take the path on the left, and walk for about an hour. ")
    print("You come upon a cabin, You knock on the door, but nobody anwers.")
    print("You open the door and walk inside the cabin. ")
    print("You notice food on the table, but it looks rotten")
    print("You walk around the cabin and find a lock door.")
    print("what do you do? ")

    choice = input("> ")

    if choice == "You look for the key":
        print("You find the key in a desk, and open the lock door")
        print("And walk through the open door")
        door()
    elif choice == "sit on the couch and fall asleep":
        sleep()
    elif choice == "You take a bit of some of the food.":
        dead("You get sick and fall to the ground ")
    else:
        choice == "You walk back to the fork in the road"
        start()

def sleep():
    print("You wake up, and look start looking for some good food.  ")
    print("You find some can foods in the cabinet. ")
    print("You find the can food opener and eat all that you can find. ")
    print("You see a fire place and light a fire with the wood present.")
    print("The front door closes and locks")
    print("What do you do?")
    open_door = False

    while True:
        choice = input("> ")

        if choice == "do nothing":
            dead("You starve to dead")
        elif choice == "pick up the ax" and not open_door:
            print("You chop the door in two")
            print("You can leave the cabin")
            open_door = True
        elif choice == "back on path" and open_door:
            start()
        else:
            print("I got no idea what that means. ")



def door():
    print("When step through the door you find yourself in a diffent world. ")
    print("The world of sci-fi the world of make believe")
    print("You walk up to a table and the man what you to play a shell game. ")
    print("The man ask you to choose between 3 cups")

    choice = input("> ")

    if choice == "cup_1":
        print("nothing there, try again")
        print("the man suffles the cups")
        door()
    elif choice == "cup_2":
        print("the ball is there")
        print("The man give you a apple")
        apple()
    elif choice == "cup_3":
        print("nothing there, try again")
        print("the man suffles the cups")
        door()
    else:
        door()

def apple():
    print("You eat the apple")
    print("How many bites did it take to finish the apple")

    choice = input("> ")

    if choice < "5":
        print("The apple was great")
    elif choice > "6":
        print("May I have another")
    else:
        print("I got no idea what that means. ")


def dead(why):
    print(why, "Did you really die or did you just become the walking dead")
    exit()


def path_in_the_middle():
    print("You take the path in the middle")
    print("You find a cave.")

    while True:
        action = input("Do you enter the cave (y/n)")
        if action == "y":
            print("You enter the dark cave")

def path_on_the_right():
    print("you take the path on the right")
    print("While walking you come upon the same fork in the path")

    for walking_in_cirle in range(1, 100):
        print("Im really lost!!!!")
    for walking_in_cirle in range(1, 100):
        print("Help!!")
    while True:
        action = input("What do you do? (camp/hunt/fish)")
        if action == "camp":
            print("You set up camp for the night")
        elif action == "hunt":
            print("You hunt for some food to eat")
        elif action == "fish":
            print("You fishing for some food")
        else:
            take_nap()

def take_nap():
    print("You fall into a deep slepp")
    print("You dream that your lost in the deep dark forest and no way out.")
    print("You find yourself in a fork in he path the goins in circle.")
    print("You wake up and find yourself in the forest living the nightmare.")
    print("Then you fall bac asleep and dream that your in a forest.")
    print("You wake up and find a cute little bear linking your ear.")
    print("You kill the bear and hope his mother does not find you.")
    print("The mother bear pops out in front on you.")

    action = input ("What do you do?  (run/shoot/screem)")


def start():
    print("You are walking in the woods, you come to fork in the path")
    print("Which path do you take? ")

    choice = input("> ")

    if choice == "path on the left":
        deep_woods()
    elif choice == "path in the middle":
        path_in_the_middle()
    elif choice == "path on the right":
        path_on_the_right()
    else:
        dead("You get lost in the woods")

start()
