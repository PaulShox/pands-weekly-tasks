# plottask.py
# A program that dispays:
#   1. A histogram of a normal distribution of 1000 values with a mean of 2 and std dev of 2, and
#   2. A plot of the function f(x)=x³ in the range 0 to 10
# Author: Paul O'Shaughnessy

# Import Libraries:
import numpy as np
from numpy import random
import matplotlib.pyplot as plt

# 1. Histogram Plot:

mean_val = 5
std_dev = 2
size = 1000

x = random.normal(loc=mean_val, scale=std_dev, size=size) # generates a normal distribution based on the values applied to the variables

plt.hist(x, bins=20, edgecolor='black')
plt.axvline(mean_val, ls='--', color='red', linewidth=1, label='Mean(μ)')
plt.title(f'Normal Distribution Plot \nN={size}, μ={mean_val}, σ={std_dev}')
plt.xlabel('Value')
plt.ylabel('Amount')
plt.legend()
plt.show()

# 2. Funtion Plot:

def f(x):
    return x**3 # a function that takes a value, x, and returns the cubed value of x

x = np.linspace(0, 10) # applies x values of 0 through 10
y = f(x) # calls the function f by applying values 0 through 10 to the function 

plt.title('Plot of funtion f(x)=x³')
plt.xlabel('x value')
plt.ylabel('x³ value')
plt.grid(True)
plt.legend()

plt.plot(x,y)
plt.show()