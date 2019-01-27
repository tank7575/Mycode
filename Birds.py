from Bird import *
print('\nClass Instance Of:\n', Bird.__doc__)

polly = Bird("Squawk, Squawk!")

print('\nNumber Of Birds:', polly.count)
print("Polly Says:", polly.talk())

harry = Bird("Tweet, tweet!")
print('\nNumber of Birds:', harry.count)
print('Harry Says:', harry.talk())
