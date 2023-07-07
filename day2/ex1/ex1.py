# read input

INPUT_PATH = './day2/input.txt'

with open(INPUT_PATH, 'r') as f:
    lines = f.readlines()
    # remove line endings
    lines = [line[:-1] for line in lines]

# solution

OPTION_CONVERT = {
    'X': 'A',
    'Y': 'B',
    'Z': 'C',
}

POINTS_PER_OPTION = {
    'A': 1,
    'B': 2,
    'C': 3,
}

OPTION_BEATS = {
    'A': 'C',
    'B': 'A',
    'C': 'B',
}

OPTION_LOOSES_TO = {v: k for k, v in OPTION_BEATS.items()}

POINTS_PER_LOSS = 0
POINTS_PER_WIN = 6
POINTS_PER_DRAW = 3

def get_game_points(my_play, opponent_play):
    if OPTION_BEATS[my_play] == opponent_play:
        return POINTS_PER_WIN
    elif OPTION_LOOSES_TO[my_play] == opponent_play:
        return POINTS_PER_LOSS
    else:
        return POINTS_PER_DRAW


my_points = 0
for line in lines:
    opponent_play, my_play = line.split(' ')
    my_play = OPTION_CONVERT[my_play]
    
    my_points += POINTS_PER_OPTION[my_play]
    my_points += get_game_points(my_play, opponent_play)
    
print(my_points)