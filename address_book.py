import pickle
import os

if not os.path.exists('/Users/connorodell/python/addresses.data'):
    address_list = {}
    ab = open('/Users/connorodell/python/addresses.data', 'wb')
    pickle.dump(address_list, ab)
    ab.close()

class Contact:
    '''Class object containing personal contact information.'''
    def __init__(self, last, first, email, phone):
        self.last = last
        self.first = first
        self.email = email
        self.phone = phone
        address_list['{} {}'.format(self.first, self.last)] = self
        ab = open('/Users/connorodell/python/addresses.data', 'wb')
        pickle.dump(address_list, ab)
        ab.close()

    def tell(self):
        print('Name: {} {}, Email: {}, Phone: {}'.format(self.first, self.last, self.email, self.phone))

while True:
    ab = open('/Users/connorodell/python/addresses.data', 'rb')
    address_list = pickle.load(ab)
    ab.close()
    user_input = input('Type lookup, modify, new contact, read, remove, or quit: ')
    if user_input == 'new contact':
        first = input('Enter first name: ')
        last = input('Enter last name: ')
        email = input('Enter contact email address: ')
        phone = input('Enter contact phone number: ')
        if '{} {}'.format(first, last) in address_list:
            print('That contact is already in your address book.')
        else:
            new_contact = Contact(last, first, email, phone)
            address_list['{} {}'.format(first, last)] = new_contact
            ab = open('/Users/connorodell/python/addresses.data', 'wb')
            pickle.dump(address_list, ab)
            ab.close()
            print('The new contact information is:')
            address_list['{} {}'.format(first, last)].tell()
    elif user_input == 'modify':
        name = input('Enter a name: ')
        if name in address_list:
            mod_type = input('Do you want to modify first, last, email, or phone? ')
            if mod_type == 'first':
                address_list[name].first = input('Enter the new first name: ')
                ab = open('/Users/connorodell/python/addresses.data', 'wb')
                pickle.dump(address_list, ab)
                ab.close()
                print('The modified contact information is: ')
                address_list[name].tell()
            elif mod_type == 'last':
                address_list[name].last = input('Enter the new last name: ')
                ab = open('/Users/connorodell/python/addresses.data', 'wb')
                pickle.dump(address_list, ab)
                ab.close()
                print('The modified contact information is: ')
                address_list[name].tell()
            elif mod_type == 'email':
                address_list[name].email = input('Enter the new email: ')
                ab = open('/Users/connorodell/python/addresses.data', 'wb')
                pickle.dump(address_list, ab)
                ab.close()
                print('The modified contact information is: ')
                address_list[name].tell()
            elif mod_type == 'phone':
                address_list[name].phone = input('Enter the new phone number: ')
                ab = open('/Users/connorodell/python/addresses.data', 'wb')
                pickle.dump(address_list, ab)
                ab.close()
                print('The modified contact information is: ')
                address_list[name].tell()
            else:
                print('That is not a valid command.')
                pass
        else:
            print('That name is not in your address book.')
    elif user_input == 'read':
        for name in address_list:
            address_list[name].tell()
    elif user_input == 'lookup':
        name = input('Enter a name: ')
        if name in address_list:
            address_list[name].tell()
        else:
            print('That name is not in your address book.')
    elif user_input == 'remove':
        name = input('Enter a name: ')
        if name in address_list:
            del address_list[name]
            ab = open('/Users/connorodell/python/addresses.data', 'wb')
            pickle.dump(address_list, ab)
            ab.close()
        else:
            print('That name is not in your address book.')
    elif user_input == 'quit':
        break
    else:
        print('That is not a valid command.')