pets = ['dog', 'cat', 'birds', 'rabbit', 'fish', 'neighbor']

print(pets[0])
print(pets[1])
print(pets[2])
print(pets[3])
print(pets[4])
print(pets[5], '\n')

for doodeledy in pets:
    print(doodeledy)

i_get_20_bucks = 20

while i_get_20_bucks < 35:
        print(i_get_20_bucks)
        i_get_20_bucks += 1
print('i need more money')

for i in range(1500, 2700):
     if i % 7 == 0 and i % 5 == 0:
        print(i)


import random
target_num, guess_num = random.randint(1,10), 0
while target_num != guess_num:
    guess_num = int(input('guess a number between 1 and 10, and keep guessing till you are right'))
print('game over')

count = 0
for num in range(7):
    count += 1
    print('*' * count)
for num in range(6):
    count -= 1
    print('*' * count)
