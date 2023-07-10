import re

# read input

INPUT_PATH = './day5/input.txt'

with open(INPUT_PATH, 'r') as f:
    lines = f.readlines()
    # remove line endings
    lines = [line[:-1] for line in lines]

# solution

MOVE_REGEX = r"(move (?P<amount>\d+) from (?P<from>\d+) to (?P<to>\d+))"

def read_stack_element(line, start_index):
    if line[start_index] == '[':
        return line[start_index + 1]
    else:
        return None

stacks = []

stack_number_line = 0
while lines[stack_number_line][:2] != ' 1':
    stack_number_line += 1

# FIXME: this does not account for stack indexes with over 2 digits, or having exactly one stack!
n_stacks = int(lines[stack_number_line][-3:].strip())

for i in range(n_stacks):
    stacks.append([])

# read initial stacks
for line in lines[:stack_number_line]:
    for i in range(n_stacks):
        stack_el = read_stack_element(line, i * 4)

        if stack_el:
            stacks[i].insert(0, stack_el)

# read and execute movements
for line in lines[stack_number_line + 2:]:
   move = re.search(MOVE_REGEX, line).groupdict()

   amount = int(move['amount'])
   source = int(move['from']) - 1
   dest = int(move['to']) - 1

   # read and execute movements
for line in lines[stack_number_line + 2:]:
   move = re.search(MOVE_REGEX, line).groupdict()

   amount = int(move['amount'])
   source = int(move['from']) - 1
   dest = int(move['to']) - 1

   letters = stacks[source][-amount:]
   stacks[source] = stacks[source][:-amount]
   stacks[dest] += letters

letters = [stack.pop() for stack in stacks]
print(''.join(letters))
