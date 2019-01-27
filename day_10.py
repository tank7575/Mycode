x = input ('Type what do you want to reverse...')
b = ''.join(reversed(x))
print(b)

print(x[::-1])

def oddEvenCount(x):
    odd_count = 0
    even_count = 0
    for i in x:
        if i % 2 == 0:
            even_count += 1
        else:
            odd_count += 1
    return "odd_count: " + str(odd_count) + "\teven count: " + str(even_count)

x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
print(oddEvenCount(x))

data = [1452, 11.23, 1 + 2j, True, 'w3resource', (0, -1), [5, 12], {'class': 'V', 'section': 'A'}]

for icecream in data:
    print('Type of ', icecream, ' is ', type(icecream))


for i in range(7):
    if i != 3 and i != 6:
        print(i)
print('\n')

x, y = 0, 1
while y < 50:
    print(y)
    x, y = y, x + y

print('\n')

for moomoo in range(1, 50):
    if moomoo % 3 == 0:
        print('Supaaa')
    if moomoo % 5  == 0:
        print('badman')
    if moomoo % 3 == 0 and moomoo % 5 == 0:
        print('superman')
    else:
        print(moomoo)
