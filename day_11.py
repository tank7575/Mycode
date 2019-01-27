row_num = int(input('How many rows: '))
col_num = int(input('How many columns: '))
list = [[0 for col in range(col_num)] for row in range(row_num)]

for row in range(row_num):
    for col in range(col_num):
        list[row][col] = row * col
print(list, '\n')

lines = []
while True:
    l = input()
    if l:
        lines.append(l.lower())
    else:
        break;
for l in lines:
    print(l)

def divividable_binary():
    s = input('Enter the binaries: ')
    l = s.split(',')
    for i in l:
        if int(str(i), 2) % 5 == 0:
            print('Output: ', i)
divividable_binary()
