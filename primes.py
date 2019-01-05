# Next Prime Number - Have the program find prime numbers until the
# user chooses to stop asking for the next one.

def factor(integer):
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
    return factors

def is_prime(integer):
    if factor(integer) == [integer]:
        return True
    else:
        return False

def primes():
    index = 2
    print('The first prime is {}'.format(index))
    while True:
        string = input('Find the next prime? (y or n): ')
        if string == 'y':
            while True:
                index += 1
                if is_prime(index) == True:
                    print('The next prime is {}'.format(index))
                    break
        else:
            break

# primes()

def primes_until_interrupt(index = 2):
    # Prints primes until interrupted (ctrl-c)
    # User may specify starting index
    try:
        while True:
            if is_prime(index) == True:
                print(index)
            index += 1
    except KeyboardInterrupt:
        pass

# primes_until_interrupt(111833)