def start():
    print("You eat the apple")
    print("How many bites did it take to finish the apple")

    choice = input("> ")

    if choice <= "6":
        print("The apple was great")
    elif choice >= "7":
        print("May I have another")
    else:
        print("I got no idea what that means. ")


start()
