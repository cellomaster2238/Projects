# Prime Factorization - Have the user enter a number and find all
# Prime Factors (if there are any) and display them.

def factor():
    integer = int(input('Enter an integer greater than 2: '))
    factors = []
    index = 2
    while index in range(2,integer + 1):
        # The loop is broken when factorization is complete
        if integer == 1:
            break
        # index is appended to factors if divides integer
        if integer % index == 0:
            factors.append(index)
            # Removes the prime factor and shortens the while loop
            integer = int(integer / index)
        else:
            # Proceed to next possible factor
            index += 1
    # Print the factorization
    print('The prime factorization of is:')
    print(factors)

factor()
