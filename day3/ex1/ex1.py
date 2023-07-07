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
for line in lines:
    middle = len(line) // 2

    # store chars in sets for O(1) rather than O(n) search(for large strings, this would make a big difference)
    items_compartment_2 = set(line[middle:])

    # we still use the string to traverse, as this is faster than using the set due to locality of reference
    common_item = next(filter(lambda l: l in items_compartment_2, line))

    priorities += get_priority(common_item)

print(priorities)
