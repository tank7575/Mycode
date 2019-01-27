x = 'blue red green'.split(' ')
print(x)
print(type(x))

A, B, C = x
print(A, B, C)

words = 'This is a random text we are going to split apart'.split(' ')
print(words)

print(input('write me a sentence:  ').split(' '))

dict = {1: 'tree', '2': 'apple', 'key': 'this is a value'}
print('this is the lenght of dict: ', str(len(dict)))
print(list(dict.keys()))

for k in dict:
    print('did this print the keys? ', k)
for k in dict:
    print('did this print the values? ', dict[k], '\n')

dict2 = {'2': 'apple', 'key':'this is a value', 1: 'tree'}
print('order is differnt but are they equal? ', dict==dict2)

list = ['tree', 'apple', 1, 'love']
list2 = ['apple', 1, 'tree', 'love']
print('order is differnt but are they equal? ', list==list2)

import random
x = random.choice(dict2)
y = random.choice(list2)
print('when calling to choose something from dict2', x)
print('when calling to choose something fro list2', y, '\n')

x = random.choice([dict2])
y = random.choice([list2])
print('when calling the physical dictionary', x)
print('when calling the physical list', '\n')

x = random.choice(['one', 'two', 'three, 2'])
print('pasing a local list: ', x)
