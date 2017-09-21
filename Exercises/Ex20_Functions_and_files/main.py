from sys import argv

script, input_file = argv
# Func prints out a file that is read
def print_all(f):
    print(f.read())
# Func seeks line 0
def rewind(f):
    f.seek(0)
# Func prints the line number on the readline iteration over one line in a file
def print_a_line(line_count, f):
    print(line_count, f.readline())
# var opens input_file, which is the argv
current_file = open(input_file)
# print statement
print("First let's print the whole file:\n")
# opens and reads input_file
print_all(current_file)
# print statement
print("Now let's rewind, kind of like a tape.")
# opens input_file and seeks line 0
rewind(current_file)
# print statement
print("Let's print three lines:")
# var current_line assigned to int 1
current_line = 1
# Print_a_line calls two variables. Line_count(1) and f(open(input_file))
# The open file is .readline, which is just that line
# The file is open, oneline is read and the whole function is printed
print_a_line(current_line, current_file)
# The above process happens again but 1 is just added
current_line += 1
print_a_line(current_line, current_file)
# The above process happens again and another 1 is added
current_line += 1
print_a_line(current_line, current_file)
