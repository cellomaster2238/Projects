# Change Return Program - The user enters a cost and then the amount of money
# given. The program will figure out the change and the number of quarters,
# dimes, nickels, pennies needed for the change.

def change(cost, amount):
    quarters, dimes, nickels, pennies = 0, 0, 0, 0
    total_change = int(100 * (amount - cost)) % 100
    remainder = total_change
    if total_change / 25 >= 1:
        quarters = int(total_change // 25)
        remainder = total_change - (25 * quarters)
    if remainder / 10 >= 1:
        dimes = int(remainder // 10)
        remainder = remainder - (10 * dimes)
    if remainder / 5 >= 1:
        nickels = int(remainder // 5)
        remainder = remainder - (5 * nickels)
    if remainder / 1 >= 1:
        pennies = int(remainder / 1)
    print('Total change is {} cents\nQuarters: {}, dimes: {}, Nickels: {}, Pennies: {}'.format(
        total_change, quarters, dimes, nickels, pennies))

change(15.75, 20)