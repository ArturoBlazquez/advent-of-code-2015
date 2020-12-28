from utils import read_file, print_part_1, binary, print_part_2


def parse_circuit():
    circuit = {}
    for line in read_file('input.txt'):
        input, output = line.split(' -> ')

        if input.isnumeric():
            circuit[output] = input
        else:
            circuit[output] = input.split(' ')

    return circuit


circuit = parse_circuit()


# -- PART 1 -- #
def complement(num):
    num_in_binary = binary(num, 16)

    num_in_binary = num_in_binary.replace('0', 'x')
    num_in_binary = num_in_binary.replace('1', '0')
    num_in_binary = num_in_binary.replace('x', '1')

    return int(num_in_binary, 2)


values = {}


def get_value(output):
    if output.isnumeric():
        return int(output)
    if output in values:
        return values[output]

    input = circuit[output]

    if not isinstance(input, list):
        values[output] = int(input)
    elif len(input) == 1:
        values[output] = get_value(input[0])
    elif input[0] == 'NOT':
        values[output] = complement(get_value(input[1]))
    elif input[1] == 'AND':
        values[output] = get_value(input[0]) & get_value(input[2])
    elif input[1] == 'OR':
        values[output] = get_value(input[0]) | get_value(input[2])
    elif input[1] == 'LSHIFT':
        values[output] = get_value(input[0]) << int(input[2])
    elif input[1] == 'RSHIFT':
        values[output] = get_value(input[0]) >> int(input[2])

    return get_value(output)


print_part_1(get_value('a'))

# -- PART 2 -- #
values = {'b': get_value('a')}

print_part_2(get_value('a'))
