a = 1
b = 2

print('\nVariable a ls :', 'One' if(a == 1) else 'Not One')
print('\nVariable a IS :' , 'Even' if(a % 2 == 0) else 'Odd')

print('\nVariable b ls :' , 'One' if(b == 1) else 'Not One')
print('\nVariable b ls :' , 'Even' if(b % 2 == 0) else 'Odd')

max = a if(a > b) else b

print('\nGreater Value ls :' ,max)
