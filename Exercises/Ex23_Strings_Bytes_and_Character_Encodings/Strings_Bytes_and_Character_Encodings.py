import sys
script, encoding, error = sys.argv


def main(language_file, encoding, errors):
    line = language_file.readline()

    if line:
        print_line(line, encoding, errors)
        return main(language_file, encoding, errors)


def print_line(line, encoding, errors):
    next_lang = line.strip()
    raw_bytes = next_lang.encode(encoding, errors=errors)
    cooked_string = raw_bytes.decode(encoding, errors=errors)

    print(raw_bytes, "<===>", cooked_string)


languages = open("languages.txt", encoding="utf-8")

main(languages, encoding, error)

# list of unfamiliar things
# encoding, error, sys.argv, .strip, .encode, .decode
# shaw runs python ex23.py utf-8 strict
# what is LaTeX
# codecs: utf-8, utf-16, big5

# Symbol list
#utf8
# xc3\xa1 = á
# xc5\xa0 = Š
# xe2\x80\xba = >
# xcb\x86 = ^
# xc3\x90 = Ð
# xc2\xb0 = °
# xc3\x92 = Ò
# xc3\x93 = Ó

# Cheats for bin/codec conversion
#0b1011010 == 90
# ord('Z') == 90
# chr(90) == 'Z'
