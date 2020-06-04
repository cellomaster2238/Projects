# Calculate the payments for a fixed term mortgage over N terms at
# given interest rate. Allow users to select compounding interval.

def mortgage_calc(principal = 0, N = 0, rate = 0, compound = 12, interactive = False):
    '''User may specify the number of compoundings per year. Default is 12 (monthly).
    The rate should be yearly rate entered in decimal form.
    If interactive is True, the user is prompted for input values.'''
    if interactive == False:
        payment = principal*rate/compound*(1+rate/compound)**N/((1+rate/compound)**N-1)
    else:
        principal = float(input('Enter the principal: '))
        N = float(input('Enter the number of payments: '))
        rate = float(input('Enter the yearly interest rate in decimal form: '))
        compound = float(input('Enter the number of compoundings per year (12 for monthly): '))
        payment = principal*rate/compound*(1+rate/compound)**N/((1+rate/compound)** N-1)
    return payment