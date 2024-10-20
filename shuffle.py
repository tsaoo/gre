import random
import sys

if(len(sys.argv) < 2):
    print('usage: shuffle.py [src file] [dest file]')

with open(sys.argv[1], "r", encoding="utf-8") as file:
    lines = file.readlines()

random.shuffle(lines)

with open(sys.argv[2], "w", encoding="utf-8") as file:
    file.writelines(lines)