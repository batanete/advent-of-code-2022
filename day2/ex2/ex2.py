# read input

INPUT_PATH = './day2/input.txt'

with open(INPUT_PATH, 'r') as f:
    lines = f.readlines()
    # remove line endings
    lines = [line[:-1] for line in lines]

# solution

POINTS_PER_OPTION = {
    'A': 1,
    'B': 2,
    'C': 3,
}

POINTS_PER_LOSS = 0
POINTS_PER_WIN = 6
POINTS_PER_DRAW = 3

OPTION_BEATS = {
    'A': 'C',
    'B': 'A',
    'C': 'B',
}

OPTION_LOOSES_TO = {v: k for k, v in OPTION_BEATS.items()}

LOSS = 'X'
DRAW = 'Y'
WIN = 'Z'

def get_game_points(my_play, opponent_play):
    if OPTION_BEATS[my_play] == opponent_play:
        return POINTS_PER_WIN
    elif OPTION_LOOSES_TO[my_play] == opponent_play:
        return POINTS_PER_LOSS
    else:
        return POINTS_PER_DRAW

def get_my_play(opponent_play, my_strategy):
    if my_strategy == WIN:
        return OPTION_LOOSES_TO[opponent_play]
    elif my_strategy == DRAW:
        return opponent_play
    elif my_strategy == LOSS:
        return OPTION_BEATS[opponent_play]
    
    raise Exception(f"Invalid strategy {my_strategy}")



my_points = 0
for line in lines:
    opponent_play, my_strategy = line.split(' ')

    my_play = get_my_play(opponent_play, my_strategy)
    
    my_points += POINTS_PER_OPTION[my_play]
    my_points += get_game_points(my_play, opponent_play)
    
print(my_points)