from utils import read_file, print_part_1, print_part_2

santa_list = read_file('input.txt')


# -- PART 1 -- #
def escape(word: str):
    ret_string = word[1:-1]

    ret_string = ret_string.replace('\\\\', '¡').replace('\\"', '"')

    while '\\x' in ret_string:
        scape_index = ret_string.index('\\x')
        ret_string = ret_string[:scape_index] + '@' + ret_string[scape_index + 4:]

    return ret_string


print_part_1(sum([len(word) for word in santa_list]) - sum([len(escape(word)) for word in santa_list]))


# -- PART 2 -- #
def encode(word: str):
    ret_string = '?' + word + '?'

    ret_string = ret_string.replace('\\', '¡¡').replace('"', '@@')

    return ret_string


print_part_2(sum([len(encode(word)) for word in santa_list]) - sum([len(word) for word in santa_list]))
