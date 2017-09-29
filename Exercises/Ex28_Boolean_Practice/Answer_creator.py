from sys import argv

script, in_file, out_file = argv

in_txt = open(in_file)
out_txt = open(out_file, "r+")

def main(in_txt, out_txt,):
    line = in_txt.readline()

    if line:
        print_line(line)
        return main(in_txt, out_txt)
 

def print_line(in_txt, out_txt):
    next_line = line.strip()

    print(f'print("{next_line}: "{next_line})')




in_txt.close()
out_txt.close()