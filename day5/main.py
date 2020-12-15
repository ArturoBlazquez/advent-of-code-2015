from utils import read_file, print_part_1, print_part_2, contains_any

strings = read_file('input.txt')


# -- PART 1 -- #
def is_nice(string):
    if contains_any(string, ['ab', 'cd', 'pq', 'xy']):
        return False

    num_vowels = sum([string.count(vowel) for vowel in ['a', 'e', 'i', 'o', 'u']])
    if num_vowels < 3:
        return False

    has_doubles = False
    previous_letter = ''

    for letter in string:
        if letter == previous_letter:
            has_doubles = True

        previous_letter = letter

    return has_doubles


nice_strings = 0
for string in strings:
    if is_nice(string):
        nice_strings += 1

print_part_1(nice_strings)


# -- PART 2 -- #
def is_nice_v2(string):
    has_pairs = False
    for i in range(len(string) - 3):
        if string[i:i + 2] in string[i + 2:]:
            has_pairs = True

    if not has_pairs:
        return False

    has_doubles = False
    previous_letter = ''
    two_previous_letter = ''

    for letter in string:
        if letter == two_previous_letter:
            has_doubles = True

        two_previous_letter = previous_letter
        previous_letter = letter

    return has_doubles


nice_strings = 0
for string in strings:
    if is_nice_v2(string):
        nice_strings += 1

print_part_2(nice_strings)
