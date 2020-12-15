from utils import read_file, print_part_1, print_part_2

input = read_file('input.txt')[0]

# -- PART 1 -- #
print_part_1(input.count('(') - input.count(')'))

# -- PART 2 -- #
floor = 0
for index, character in enumerate(input, start=1):
    if character == '(':
        floor += 1
    else:
        floor -= 1

    if floor == -1:
        break

print_part_2(index)
