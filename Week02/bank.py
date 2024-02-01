# bank.py
# This program requests two amounts in cents, adds them together and returns a message "The sum of these is" with the amount converted to a euro amount
# Author: Paul O'Shaughnessy


cent1 = int(input('Enter amount1 (in cent): '))
cent2 = int(input('Enter amount2 (in cent): '))
total = ((cent1 + cent2)/100)
totalr = "{:.2f}".format(total) # to ensure trailing zeroes are kept, e.g 60 + 70 returned €1.3. I want it to return €1.30
print('The sum of these is €' + str(totalr))