day = 32

try:
        if day > 31:
                raise ValueError('Invalid Day Number')
        #more statements to excute get added here
except ValueError as msg:
        print('The Program Found An', msg)

finally:
        print('But Today is Beautiful Anyway.')
