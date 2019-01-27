from Bird import *
print('\nClass Instance of:\n', Bird.__doc__)

polly = Bird("Squawk, Squawk!")

print('\nNumber of birds:', polly.count)
print('Polly Says:', polly.talk())

harry = Bird('Tweet, Tweet!')

print('\nNumber of Birds:', harry.count)
print('Harry Says:', harry.talk())
