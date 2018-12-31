# Find e to the Nth Digit - Just like the previous problem, but with e instead
# of PI. Enter a number and have the program generate e up to that many decimal
# places. Keep a limit to how far the program will go.

import math

def e_decimal():
    '''Prints a decimal approximation of e up to a user selected accuracy'''
    integer = input('Enter an integer between 0 and 30 (inclusive): ')
    try:
        if int(integer) in range(0,31):
            print(format(math.e, '.' + integer + 'f'))
        else:
            print('Invalid input')
    except ValueError:
        print('Invalid input')

e_decimal()