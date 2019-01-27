letter_s = ''
for row in range(7):
    for col in range(7):
        if ((row == 0 or row == 3 or row == 6) and col > 0 and col < 7):
            letter_s = letter_s + '*'
        elif ((row == 1 or row == 2) and col == 1):
            letter_s = letter_s + '*'
        elif ((row == 4 or row == 5) and col == 6):
            letter_s = letter_s + '*'
        else:
            letter_s = letter_s + ' '
    letter_s = letter_s + '\n'
print(letter_s)

x = ''
for row in range(0, 7):
    for column in range(0, 7):
        if (((column == 1 or column == 5) and (row > 4 or row < 2)) or row == column and column > 0 and column < 6 or (column == 2 and row  == 4 ) or (column == 4 and row == 2)):
            x = x + "*"
        else:
            x = x + " "
    x = x + '\n'
print(x)

human = int(input ('How many human years has the dog been alive?'))

if human < 0:
    print('age must be a positive number')
    exit()
elif human <= 2:
    dog_age = human * 10.5
else:
    dog_age = 21 + (human - 2) * 4
print("the dog's age in dog's years is :", dog_age)

x = input('choose any letter from the alphabet:')
if x in ('a', 'e','i','o','u'):
    print('{} is a vowel'.format(x))
elif x == 'y':
    print('A, E, I, O, U and sometime Y')
else:
    print('{} is a consontant'.format(x))

months = ['January', 'February', 'March', 'April', 'May', 'July', 'Auguest',
        'September', 'October', 'November', 'December']

print('Lists of Months: ', months)
month = input('Give me a month:')
if month == 'February':
    print('Number of 28/29')
elif month in ('April', 'June', 'September', 'November'):
    print('Number of days: 30 days')
elif month in ('January', 'March', 'May', 'July', 'Auguest', 'October', 'December'):
    print('Number of days: 31 days')
else:
    print('type the month better!!!!')
