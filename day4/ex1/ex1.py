# read input

INPUT_PATH = './day4/input.txt'

with open(INPUT_PATH, 'r') as f:
    lines = f.readlines()
    # remove line endings
    lines = [line[:-1] for line in lines]

# solution

def contains(r1, r2):
    return r2[0] >= r1[0] and r2[1] <= r1[1]

matches = 0

for line in lines:
    r1_raw, r2_raw = line.split(',')
    
    r1_raw = r1_raw.split('-')
    r1 = (int(r1_raw[0]), int(r1_raw[1]))

    r2_raw = r2_raw.split('-')
    r2 = (int(r2_raw[0]), int(r2_raw[1]))

    if contains(r1, r2) or contains(r2, r1):
        matches += 1

print(matches)
