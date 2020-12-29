from itertools import groupby

from utils import read_file, print_part_1, print_part_2

start_sequence = read_file('input.txt')[0]


# -- PART 1 -- #
def look_and_say(sequence: str):
    return ''.join(str(len(list(g))) + k for k, g in groupby(sequence))


sequence = start_sequence
for i in range(40):
    sequence = look_and_say(sequence)

print_part_1(len(sequence))

# -- PART 2 -- #
for i in range(10):
    sequence = look_and_say(sequence)

print_part_2(len(sequence))
