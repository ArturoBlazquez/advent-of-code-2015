from utils import read_file, print_part_1, print_part_2

instructions = read_file('input.txt')[0]

# -- PART 1 -- #
x_position = 0
y_position = 0
houses_visited = set()
houses_visited.add((0, 0))

for instruction in instructions:
    if instruction == '^':
        x_position += 1
    elif instruction == 'v':
        x_position -= 1
    elif instruction == '>':
        y_position += 1
    elif instruction == '<':
        y_position -= 1

    houses_visited.add((x_position, y_position))

print_part_1(len(houses_visited))

# -- PART 2 -- #
santa_x_position = 0
santa_y_position = 0
robot_x_position = 0
robot_y_position = 0

houses_visited = set()
houses_visited.add((0, 0))

for i in range(0, len(instructions), 2):
    instruction = instructions[i]

    if instruction == '^':
        santa_x_position += 1
    elif instruction == 'v':
        santa_x_position -= 1
    elif instruction == '>':
        santa_y_position += 1
    elif instruction == '<':
        santa_y_position -= 1

    houses_visited.add((santa_x_position, santa_y_position))

for i in range(1, len(instructions), 2):
    instruction = instructions[i]

    if instruction == '^':
        robot_x_position += 1
    elif instruction == 'v':
        robot_x_position -= 1
    elif instruction == '>':
        robot_y_position += 1
    elif instruction == '<':
        robot_y_position -= 1

    houses_visited.add((robot_x_position, robot_y_position))

print_part_2(len(houses_visited))
