from Bird import *

chick = Bird('Cheep! Cheep')
chick.age = '1 week'

print('\nChick Says:', chick.talk())
print('chick Age:', chick.age)

chick.age = '2 weeks'
print('Chick now:', chick.age)

setattr(chick, 'age', '3 weeks')

print('\nChick Attributes..')
for attrib in dir(chick):
      if attrib[0]!='_':
          print(attrib, ':', getattr(chick, attrib))

delattr(chick, 'age')
print('\nChick age Attribute?', hasattr(chick, 'age'))
