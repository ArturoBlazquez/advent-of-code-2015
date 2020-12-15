from utils import read_file, print_part_1, print_part_2
from hashlib import md5

secret_key = read_file('input.txt')[0]

# -- PART 1 -- #
num = 0
while 1:
    hash = md5((secret_key + str(num)).encode('utf-8')).hexdigest()
    if hash[:5] == '00000':
        break

    num += 1

print_part_1(num)

# -- PART 2 -- #
while 1:
    hash = md5((secret_key + str(num)).encode('utf-8')).hexdigest()
    if hash[:6] == '000000':
        break

    num += 1

print_part_2(num)
