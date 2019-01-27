print(""" You enter a dark room with three doors.
Do you go through door #1 or door #2 or door #3""")

door = input("> ")

if door =="1":
    print("There's a giant bear here eating a cheese cake.")
    print("What do you do?")
    print("1.  Take the cake.")
    print("2.  Scream at the bear!")
    print("3.  Shoot the bear!!!")

    bear = input("> ")

    if bear == "1":
        print("The bear eats your face off.  Good jobs!")
        print("What do you do?")
        print("1.  Spit in his face.")
        print("2.  Lick his face.")
        print("3.  Ask him to give it back.")

        bear = input("> ")

        if bear == "1":
            print("The bear spits back")
        elif bear == "2":
            print("The bear lick your face")
        else:
            print("The bear gives back your face")
    elif bear == "2":
        print("The bear eats your legs off.  Good Jobs!")
        print("What do you do?")
        print("1.  Shoot him in the face.")
        print("2.  Give him your other leg to eat.")

        bear = input("> ")

        if bear == "1":
            print("The bear gets angry.")
        elif bear == "2":
            print("He turns away from it.")
    elif bear == "3":
        print("The Bear dies!!!!")
        print("Do you eat the bear and skin him or do nothing.")
        print("1.  Eat the bear and skin him.")
        print("2.  Do nothing!!")

        bear = input("> ")

        if bear == "1":
            print("Take a nap!!")
        elif bear == "2":
            print("Eat the Cake!!!")
    else:
        print(f"Well, doing {bear} is probably better.")
        print("Bear runs away.")
elif door == "2":
    print("Your stare into the endless abyss at Cthulhu's retina")
    print("1.  Blueberries.")
    print("2.  Yellow jacket clothesns.")
    print("3.  Understanding revolvers yelling melodies.")


    insanity = input("> ")

    if insanity == "1" or insanity == "2":
        print("Your body survives powered by a mind of jello.")
        print("Good Job!")
    else:
        print("You stuble around the fall on a knife and die. Good Job!! ")

else:
    print("A house of full of Zombies!!!")
    print("What do you do?")
    print("#1.  Pick up the Bat.")
    print("#2.  Run out the door.")
    print("#3.  Run through the Zombies.")


    Zombies = input ("> ")

    if Zombies == "1":
        print("You take the heads off the Zombies!!!")
    elif Zombies == "2":
        print("And run into Bear that is eating cakes")
    else:
        print("Zombies eat your brains!!")
