def check_guess(guess, answer):
    global score
    still_guessing = True
    attempt = 0
    print(">>>> still_guessing=", still_guessing)
    while still_guessing and attempt < 1:
        if guess.lower() == answer.lower():
            print("Correct answer")
            score = score + 3 - attempt
            still_guessing = False
        else:
            if attempt < 1:
                guess = input("Sorry wrong answre.  Try again.  ")
            attempt = attempt + 1

    if attempt == 1:
        print("The correct answer is " + answer)

score = 0
print("Guess the Animal!")
guess1 = input("Which bear lives at the North Pole? \n")
check_guess(guess1, "polar bear")
guess2 = input("Which is the fastest land animal? \n")
check_guess(guess2, "cheetah")
guess3 = input("Which is the largest animal? \n")
check_guess(guess3, "blue whale")
guess4 = input("Which one of these is a fish?  \n \
A) Whale\n B) Dolphin\n C) Shark\n D) Squid\n \
Type A, B, C, or D \n ")
check_guess(guess4, 'C')
guess5 = input("Mice are Mammals.\nTrue or False \n")
check_guess(guess5, "True")

print("Your score is " + str(score))
