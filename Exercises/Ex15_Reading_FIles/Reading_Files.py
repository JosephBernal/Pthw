# Importing argv from the system module
from sys import argv

# argv takes two variables named filename and script
script, filename = argv

# The variable txt opens filename, which is an argv variable
txt = open(filename)

# filename is entered after this prompt, which is then assigned to the variable txt. At the same time this has to be a valid filename. In a better program we would add an exception saying something like can not find  your file try again instead of exiting the program.
print(f"Here's your file {filename}:")

# The newly formed variable txt is then printed into the shell environment
print(txt.read())

# The program continues with another prompting statement
print("Type the filename again:")

# This time instead of using argv we are using a custom input, which makes it look like it is in the python program also we are assigning file_again to this input
file_again = input("> ")

# That input then has the method open operated on it and assigned to the variable txt_again, so in actuality the file has not been opened. But instead just assigned to a variable
txt_again = open(file_again)

# This is where python reads the opened txt_again file and prints its contents.
print(txt_again.read())

# In summary the process to print the contents of a file to the command shell is to open the file, read the file, then print what was read.

txt.close()
txt_again.close()
