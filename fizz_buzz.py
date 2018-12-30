# Fizz Buzz - Write a program that prints the numbers from 1 to 100.
# But for multiples of three print “Fizz” instead of the number and
# for the multiples of five print “Buzz”. For numbers which are
# multiples of both three and five print “FizzBuzz”.

for index in range(1,101):
    if index % 3 == 0 and index % 5 == 0:
        print('FizzBuzz')
    elif index % 3 == 0:
        print('Fizz')
    elif index % 5 == 0:
        print('Buzz')
    else:
        print(index)