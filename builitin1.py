from Bird import *

zola = Bird('Beep, beep!')

print('\nBuilt-in Instance Attriubtes...')
for attrib in dir(zola):
    if attrib[0] == '_':
        print(attrib)

print('\Class Dictionary...')
for item in Bird.__dict__:
    print(item, ':', Bird.__dict__[item])

print('\nInstance Dictionary...')
for item in zola.__dict__:
        print(item, ':', zola.__dict__[item])
