import numpy as np
print(np.__version__)


list = [12, 998, 45.73, 9, 7, 21, 0.6]
print('Starting list: ', list)

one_d_array = np.array(list, dtype = int)
print('My First 1 Dimensional Array: ', one_d_array)

x = np.arange(2, 11).reshape(3, 3)
print(x)

y = np.arange(2, 11, 2)
print(y)

x = np.zeros(10, dtype=int)
print(x)
x[[3, 6]] = 21
print(x)

x =np.arange(7, 21)
print(x)
x = x[::-1]
print(x)
