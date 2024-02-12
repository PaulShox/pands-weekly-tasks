# accounts.py
# Two programs. The first requests a 10 digit number and returns it with only the last four digits visible, the rest converted to X. 
# The second returns the same format but for any amount of digits.
# Author: Paul O'Shaughnessy

# Program 1:
ac = input('Please enter a 10 digit number: ') # left as a string as no numeric calcs and assists with concatenation on 2nd last line
while len(ac) != 10:
    ac = input('must be a 10 digit number: ') # to ensure only 10 digits are entered

ac1 = 'xxxxxx' + ac[-4:] # first 6 digits will always be converted to x so can be concatenated to the last 4 digits in string format 
print(ac1)


# Program 2:
ac = input('Please enter an account number of any length: ')
if len(ac) < 4:
    ac = input('must be at least 4 digits: ') # in order to return the last four digits, the digit input has to be at least 4 digits

ac2 = 'x' * len(ac[:-4]) # once the length of the digit string is established up to the last 4 digits, it gets multiplied by x, which as a string returns that number x's
print(ac2 + ac[-4:])