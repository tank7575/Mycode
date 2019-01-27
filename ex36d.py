backpack = ["rope", "knive", "compass", "water bottle", "watch",
            "clothes", "shoes", "tent", "gloves"]

rules = ['stay on path',
        'drink plenty of water',
        'don\'t feed animail',
        'don\'t litter',
        'do pick up trash']
people = {"LT": "Luke",
        "LAT": "Lori",
        "BC": "Bill",
        "JS": "Jon",
        "LA": "Lonnie",
        "JD": "John"
        }

trees = {"pine": "pn",
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
    print(f"You pull out your backpack which is filled with {backpack}")



def dead(why):
    print(why, "Did you really die or did you just become the walking dead")
    exit()

def start():
    print("You are walking in the woods, you come to fork in the path")
    print("Which path do you take? ")

    choice = input("> ")

    if choice == "left":
        deep_woods()
    elif choice == "middle":
        path_in_the_middle()
    elif choice == "right":
        path_on_the_right()
    else:
        dead("You get lost in the woods")

start()
