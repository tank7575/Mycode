import random
import string

adjectives = ['sleep', 'slow', 'smelly',
                'wet', 'fat', 'red',
                'orange', 'yellow', 'green',
                'blue', 'purple', 'fluffy',
                'white', 'proud', 'brave',
                'hard', 'soft', 'dark']

nouns = ['apple', 'dinosaur', 'ball',
        'toaster', 'goat', 'dragon',
        'hammer', 'duck', 'panda',
        'dog', 'house', 'pizza',
        'jackel', 'notebook', 'scotland',
        'paper', 'cardboard', 'network']

print("Welcome to Password Picker!")

adjectives = random.choice(adjectives)
noun = random.choice(nouns)
number = random.randrange(0, 100)
specical_char = random.choice(string.punctuation)

password = adjectives + noun + str(number) + specical_char
print("Your new password is: %s" % password)
