# collatz.py
# A program to run the Collatz conjecture - a famous mathematical problem. The program requests the user to provide a positive number, and then outputs the next lower number by taking the current value and dividing by two if positive, multiplying it by three and adding one if negative.
# Author: Paul O'Shaughnessy

num = int(input('Enter a positive integer number: '))
print (num, end = ' ') # end = ' ' ensures the figures are returned on a single line with a space between them
while num != 1:
    if num % 2 == 0:
        num = round(num / 2)
        print(num, end = ' ')
    else:
        num = round(num * 3 + 1) 
        print(num, end = ' ') 