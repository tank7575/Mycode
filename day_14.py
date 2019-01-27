month = input('Type in month: ')
day = int(input('Select a numerical day'))

x = ['January', 'February', 'March']
y = ['April', 'May', 'June']
z = ['July', 'Auguest', 'September']

if month in (x):
    season = 'wenter'
elif month in (y):
    season = 'spring'
elif month in (z):
    season = 'summer'
else:
    season = 'autumn'

if (month == 'March') and (day > 19):
    season = 'spring'
elif (month == 'June') and (day > 20):
    season == 'summer'
elif (month == 'September') and (day > 21):
    season == 'autumn'
elif (month == 'December') and (day > 20):
    seaosn == 'winter'

print('Season is', season)

month = input('What is the month of your birth: ')
day = int(input('What is numerical day of Birthday: '))

if month == 'December':
    sign = 'Sag' if day < 22 else "cap"
elif month == 'January':
    sign = 'cap' if day < 20 else 'aqu'
elif month == 'February':
    sign = 'aqu' if day < 19 else 'pis'
elif month == 'March':
    sign = 'pis' if day < 21 else 'aris'
elif month == 'April':
    sign = 'aris' if day < 20 else 'taur'
elif month == 'May':
    sign = 'taur' if day < 21 else 'gem'
elif month == 'June':
    sign = 'gem' if day < 21 else 'canc'
elif month == 'July':
    sign = 'canc' if day < 23 else 'leo'
elif month == 'Augest':
    sign = 'leo' if day < 23 else 'virgo'
elif month == 'September':
    sign = 'virgo' if day < 23 else 'libra'
elif month == 'October':
    sign = 'libra' if day < 23 else 'scor'
elif month == 'November':
    sign = 'scor' if day < 22 else 'Sag'

print('your sign from the stars is :', sign)

a = float(input('first number: '))
b = float(input('second number: '))
c = float(input('third number: '))

if a > b:
    if a < c:
        median = a
    elif b > c:
        median = b
    else:
        median = c
else:
    if a > c:
        median = a
    elif b < c:
        median = b
    else:
        median = c
print('the median is: ', median)
