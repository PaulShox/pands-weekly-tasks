# text_file_count.py
# A program to read a text file from the Command Line, and then to count the number of letter e's in the text.
# Author: Paul O'Shaughnessy

import sys # https://docs.python.org/3/library/sys.html#module-sys
import os # https://docs.python.org/3/library/os.path.html#module-os.path

# python text_file_count.py mobydick.txt is what gets input in the Command Line

my_text_file = sys.argv[1] 
# sys.argv reads the list of command line arguments passed to a Python script. 
# the text file is the second argument in the Command Line, so index/position [1]
# https://www.youtube.com/watch?v=ZQ9JO0e9468

if len(sys.argv) !=2:
   print('Please enter 2 arguments: python file name, text file name')
   exit()
# this checks the correct amount of arguments are in the Command Line 
# only 2 arguments should be in the Command Line:
# the python file itself, and the txt file

if os.path.exists(my_text_file):
    pass
else:
    print('text file does not exist')
# checks the file being read exists

with open(my_text_file, 'r') as f:
    text = f.read()
    text1 = text.count('e')
# counts the number of the letter e in the file being read

print(text1)





