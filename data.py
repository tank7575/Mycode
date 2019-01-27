import pickle, os

if not os.path.isfile('pickled.dat'):
    data = [0, 1]
    data[0] = input('Enter Topic: ')
    data[1] = input('Enter Series: ')

file =open('pickle.dat', 'wb')

pickle.dump(data, file)

file.close()

file = open('pickle.dat', 'rb')

data = pickle.load(file)
file.close()

print('\nWelcome Back to:', data[0], data[1])
