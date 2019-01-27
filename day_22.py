test = int('1010', 4)
print(test)


x, y = (0, 1)
while y < 50:
    print(x, y)
    x, y = y, x + y
    print(x, y)
