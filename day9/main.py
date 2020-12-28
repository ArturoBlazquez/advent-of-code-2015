from tsp_solver.greedy import solve_tsp
from tsp_solver.util import path_cost

from utils import read_file, print_part_1, print_part_2

distances_unparsed = [int(line.split(' = ')[1]) for line in read_file('input.txt')]

# -- PART 1 -- #
distances = [[] for _ in range(8)]

for i in range(7):
    for j in range(7-i):
        distances[i+1+j].append(distances_unparsed[j])
    distances_unparsed = distances_unparsed[7-i:]

path = solve_tsp(distances)

print_part_1(path_cost(distances, path))

# -- PART 2 -- #
for i in range(len(distances)):
    for j in range(len(distances[i])):
        distances[i][j] = 1000 - distances[i][j]

path = solve_tsp(distances)

print_part_2(1000 * (len(path) - 1) - path_cost(distances, path))
