import re

# read input

INPUT_PATH = './day6/input.txt'

with open(INPUT_PATH, 'r') as f:
    line = f.read()

# solution

for i, c in enumerate(line[3:]):
    word = line[i:i + 4]

    if len(set(word)) == len(list(word)):
        print(i + 4)
        break
