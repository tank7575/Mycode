from Bird import *

zola = Bird("Beep, Beep")

print("\nBuilt-in Instance Attribues...")
for attrib in dir(zola):
    if attrib[0] == '_':
            print(attrib)

print("\nClass Dictionary...")
for item in Bird.__dict__:
    print(item, ':', Bird.__dict__[item])

print('\nInstance Dictionary...')
for item in zola.__dict__:
        print(item, ':', zola.__dict__[item])
