from utils import read_file, print_part_1, print_part_2

dimensions = [[int(x) for x in line.split('x')] for line in read_file('input.txt')]

# -- PART 1 -- #
feet_of_wrapping_paper = 0
for dimension in dimensions:
    l, w, h = dimension

    feet_of_wrapping_paper += 2 * (l * w + w * h + h * l)

    if max(l, w, h) == l:
        feet_of_wrapping_paper += w * h
    elif max(l, w, h) == w:
        feet_of_wrapping_paper += l * h
    else:
        feet_of_wrapping_paper += l * w

print_part_1(feet_of_wrapping_paper)

# -- PART 2 -- #
feet_of_ribbon = 0
for dimension in dimensions:
    l, w, h = dimension

    feet_of_ribbon += l * w * h

    if max(l, w, h) == l:
        feet_of_ribbon += 2 * (w + h)
    elif max(l, w, h) == w:
        feet_of_ribbon += 2 * (l + h)
    else:
        feet_of_ribbon += 2 * (l + w)

print_part_2(feet_of_ribbon)
