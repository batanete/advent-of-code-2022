INPUT_PATH = './day1/input.txt'

with open(INPUT_PATH, 'r') as f:
    lines = f.readlines()
    # remove line endings
    lines = [line[:-1] for line in lines]

totals = []
totals_curr = 0
for line in lines:
    if not line:
        totals.append(totals_curr)
        totals_curr = 0
    else:
        totals_curr += int(line)

# Possible optimization: figure out the top3 when traversing array rather than with sort(then this would be O(n) instead of O(nlog(n))
list.sort(totals)

result = sum(totals[-3:])
print(result)
