# read input

INPUT_PATH = './day3/input.txt'

with open(INPUT_PATH, 'r') as f:
    lines = f.readlines()
    # remove line endings
    lines = [line[:-1] for line in lines]

# solution

def get_priority(item):
    if item <= 'z' and item >= 'a':
        return ord(item) - ord('a') + 1
    else:
        return ord(item) - ord('A') + 27

priorities = 0
line_ind = 0
while line_ind != len(lines):
    curr_lines = lines[line_ind: line_ind + 3]
    
    curr_line = curr_lines[0]
    # store chars in sets for O(1) rather than O(n) search(for large strings, this would make a big difference)
    line2_set = set(curr_lines[1])
    line3_set = set(curr_lines[2])

    for l in curr_line:
        if l in line2_set and l in line3_set:
            priorities += get_priority(l)
            break


    line_ind += 3

print(priorities)
