# squareroot.py
# A program that uses Newton's method for estimating square roots
# Author: Paul O'Shaughnessy

# Newton Method calculation process for square roots:
# Step 1 is to approximate the square root of the number as half the number (approx_root).
# Step 2 is to add the approximate root to the original number, divide by the approximate number, and multiply by one half (next_root).
# Step 3 is to keep doing Step 2 as long as the approx_root and next_root do not equal zero (While loop).
# Step 4 is when they do equal zero, the next_root figure is printed.
# - https://surajregmi.medium.com/how-to-calculate-the-square-root-of-a-number-newton-raphson-method-f8007714f64

def sqrt(num):
    approx_root = 0.5 * num
    next_root = 0.5 * (approx_root + num/approx_root)
    while next_root != approx_root:
        approx_root = next_root
        next_root = 0.5 * (approx_root + num/approx_root)    
    return next_root


num = float(input('Please enter a positive number: '))
root = sqrt(num) # assigning a variable to the returned value of the function sqrt 
print(f'The square root of', num, 'is approx.', root)

