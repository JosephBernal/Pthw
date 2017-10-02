from sys import argv

script, filename, target = argv

target = open(target, "r+")
txt = open(filename, "r")

def answer_sheet(target):
    line = txt.readline()
    while line[0] != '#':
        target.write(f"print('{line}')\n")
    target.close()
    Questions.py.close()

answer_sheet(target)
