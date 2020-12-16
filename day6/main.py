import numpy as np

from utils import read_file, print_part_1, print_part_2


def parse_instructions():
    instructions = []
    for line in read_file('input.txt'):
        rest, finish_coordinates_text = line.split(' through ')
        end_coordinates = [int(a) for a in finish_coordinates_text.split(',')]

        start_coordinates = [int(a) for a in rest.split()[-1].split(',')]
        if 'turn on' in rest:
            instructions.append({'on': [start_coordinates, end_coordinates]})
        elif 'turn off' in rest:
            instructions.append({'off': [start_coordinates, end_coordinates]})
        else:
            instructions.append({'toggle': [start_coordinates, end_coordinates]})

    return instructions


instructions = parse_instructions()

# -- PART 1 -- #
lights_grid = np.zeros((1000, 1000), dtype=bool)

for instruction in instructions:
    command, coordinates = list(instruction.items())[0]
    row_start = coordinates[0][0]
    col_start = coordinates[0][1]
    row_end = coordinates[1][0] + 1
    col_end = coordinates[1][1] + 1

    coordinates = np.index_exp[row_start:row_end, col_start:col_end]
    if command == 'on':
        lights_grid[coordinates] = 1
    elif command == 'off':
        lights_grid[coordinates] = 0
    else:
        lights_grid[coordinates] = np.bitwise_not(lights_grid[coordinates])

print_part_1(np.sum(lights_grid))

# -- PART 2 -- #
lights_grid = np.zeros((1000, 1000), dtype=int)

for instruction in instructions:
    command, coordinates = list(instruction.items())[0]
    row_start = coordinates[0][0]
    col_start = coordinates[0][1]
    row_end = coordinates[1][0] + 1
    col_end = coordinates[1][1] + 1

    coordinates = np.index_exp[row_start:row_end, col_start:col_end]
    if command == 'on':
        lights_grid[coordinates] += 1
    elif command == 'off':
        lights_grid[coordinates] = np.clip(lights_grid[coordinates] - 1 , 0, None)
    else:
        lights_grid[coordinates] += 2

print_part_2(np.sum(lights_grid))
