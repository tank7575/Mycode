from sys import exit

def gold_room():
    print("The room is full of gold.  How much do you take?")

    choice = input("> ")
    if "0" in choice or "1" in choice:
        how_much = int(choice)
    else:
        dead("Man, learn to type a number.")

    if how_much < 50:
        print("Nice, you're not greedy, you win!")
        exit(0)
    else:
        dead("You greddy bastard!")



def bear_room():
    print("There is a bear here.")
    print("The bear has a bunch of honey.")
    print("The fat bear is in front of another door.")
    print("How are you going to move the bear.")
    bear_moved = False

    while True:
        print(">>>> bear_moved=", bear_moved)
        choice = input("> ")

        if choice == "take honey":
            dead("The bear looks at you then slaps your face off. ")
        elif choice == "taunt bear" and not bear_moved:
            print("The bear has moved from the door. ")
            print("You can go through it now. ")
            bear_moved = True
        elif choice == "taunt bear" and bear_moved:
            dead("The bear gets pissed off and chews your leg off.")
        elif choice == "open door" and bear_moved:
            gold_room()
        else:
            print("I got no idea what that means. ")


def cthulhu_room():
    print("Here you see the great evil Cthulhu. ")
    print("He, it, whatever stares at you and you go insane. ")
    print("Do you flee for your life or eat your head? ")

    choice = input("> ")

    if "flee" in choice:
        start()
    elif "head" in choice:
        dead("Well that was tasty! ")
    else:
        cthulhu_room()
def zombies():
    print("You open in front of you and there is a horde of zombies.")
    print("You see a baseball bat next to the door so you pick it up and \
    \nstart swingig throught the horde of zombies.once done you find yourself \
    \nin brains and blood")
    print("And then you look across the room and you see your best friends \
    \nBill and Dave")
    print("Your run across the room and you trip over the bodines of the dead.\
    \nYou pick yourself up and find that you no longer see your friends.")
    print("What do you do?")

    choice = input("> ")

    if choice == "Turn right":
        print("Nothing there")
    elif choice == "Turn left":
        print("Nothing there")
    elif choice == "Turn around":
        print("Your friends a right behind you")
        print("But there not the same")
        print("What do you do?")

        choice = input("> ")

        if choice == "Do nothing":
            print("Your face is bit off by your frined")
        elif choice == "Smack them around":
            print("Your frined get mad at you.")
        elif choice == "Smack them with a bat":
            print("Your friends get really mad")
        else:
            start()



def dead (why):
    print(why, "Good job!")
    print("But did you die or did you become a zombie")
    exit()

def start():
    print("You are in the dark room.")
    print("There is a door to your right and left or straight. ")
    print("Which one do you take? ")

    choice = input("> ")

    if choice == "left":
        bear_room()
    elif choice == "right":
        cthulhu_room()
    elif choice == "straight":
        zombies()
    else:
        dead("You stumble around the room unitl you starve. ")


start()
