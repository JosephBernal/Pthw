from sys import argv

script, in_file, out_file = argv

in_txt = open(in_file)
out_txt = open(out_file, "r+")


def main(in_txt, out_txt):
    line = in_txt.readline()

    if line:
        print_line(line, out_txt)
        return main(in_txt, out_txt)

def print_line(line, out_txt):
    next_line = line.strip()
    out_txt.write(f'print("{next_line}: "{next_line}) \n')



main(in_txt, out_txt)

in_txt.close()
out_txt.close()