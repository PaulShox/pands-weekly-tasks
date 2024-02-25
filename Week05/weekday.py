# weekday.py
# A program that outputs whether today is a weekday or the weekend
# Author: Paul O'Shaughnessy

import datetime
from datetime import date, time, datetime # https://realpython.com/python-datetime/

wday = [0, 1, 2, 3, 4]   # weekdays in python are 0 for Monday to 4 for Friday. wday variable creates a list for those values
today = date.today()     # this will return todays date
dayval = today.weekday() # this will reference todays date and return the relevant Python day number, e.g. 0 for Monday, 1 for Tuesday, etc.

if dayval in wday:       # "in" will check if the dayval value is in the list of weekday values. if it is, the first line below will be printed; if not, the second line will be printed
    print('Yes, unfortunately today is a weekday')
else:
    print('It is the weekend, yay!')
    
