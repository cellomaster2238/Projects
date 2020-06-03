# Fibonacci Sequence - Enter a number and have the program generate the Fibonacci
# sequence to that number or to the Nth number.

def fibonacci():
    fib_list = [0, 1]
    integer = input('Enter a non-negative integer: ')
    try:
        for index in range(2, int(integer) + 1):
            fib_list.append(fib_list[index - 1] + fib_list[index - 2])
        print('The Fibonacci sequence to the {}th number (starting at 0) is:'.format(integer))
        print(fib_list[0:int(integer) + 1])
    except:
        print('The input was not valid.')

fibonacci()
