import re

# read input

INPUT_PATH = './day6/input.txt'

with open(INPUT_PATH, 'r') as f:
    line = f.read()

# solution

PACKET_SIZE = 14

for i, c in enumerate(line[PACKET_SIZE - 1:]):
    word = line[i:i + PACKET_SIZE]

    if len(set(word)) == len(list(word)):
        print(i + PACKET_SIZE)
        break
