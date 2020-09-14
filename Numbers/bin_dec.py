# Prompt: Develop a converter to convert a decimal number to binary or a binary number to its decimal equivalent.
# Solution: Using commandline prompts and built in coverter functions

def converter():
    '''Converter for binary to decimal and decimal to binary'''

    mode = input("Enter 'bintodec' to convert binary to decimal or 'dectobin' to convert decimal to binary: ")
    if mode == 'bintodec':
        number = input('Enter a binary number: ')
        print(int(number, 2))
    if mode == 'dectobin':
        number = input('Enter a decimal number: ')
        print(bin(int(number))[2:])

converter()