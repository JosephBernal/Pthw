from sys import argv

script, in_file, out_file = argv

in_txt = open(in_file)
out_txt = open(out_file, "r+")

def main(in_file, out_file,):
    line = in_txt.readline()
 

def print_line(in_file, out_file):
    next_line = line.strip()
    print(f'print("{line}")')



in_txt.close()
out_txt.close()