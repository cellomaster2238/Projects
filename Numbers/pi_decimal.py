# Find PI to the Nth Digit - Enter a number and have the program
# generate PI up to that many decimal places. Keep a limit to how
# far the program will go.

import math

def pi_decimal():
    '''Prints a decimal approximation of pi up to a user selected accuracy'''
    integer = input('Enter an integer between 0 and 30 (inclusive): ')
    try:
        if int(integer) in range(0,31):
            print(format(math.pi, '.' + integer + 'f'))
        else:
            print('Invalid input')
    except ValueError:
        print('Invalid input')

pi_decimal()
