
from sys import argv
# read the WYSS section for how to run this
# argv takes outside arguments and applies them to this program
# On the command line you can add more than three arguments but not fewer
script, first, second, third = argv

# These will print the outcome of those three arguments
print("The script is called:", script)
print("Your first variable is:", first)
print("Your second variable is:", second)
print("Your third variable is:", third)

# A sample command line execute would look like:
# python Ex13_Parameters_Unpacking_Variables.py hello, this, argument
