import numpy as np
from collections import Counter

input_grid = np.loadtxt('data/day3.txt', comments=None, dtype=np.str).reshape(-1, 1)


def count_trees(grid, step):
    slope = step[1] / step[0]

    traverse = slope * grid.shape[0]
    repeats = int(traverse / len(grid[0]))
    full_grid = np.tile(grid, (1, repeats + 1))
    full_grid = np.array([''.join(row) for row in full_grid])

    route = [full_grid[0][0]]
    for i in range(1, int(full_grid.shape[0]/step[0])):
        next_element = i * step
        route.append(full_grid[next_element[0]][next_element[1]])

    return Counter(route)['#']


trees = []
steps = np.array([[1, 1], [1, 3], [1, 5], [1, 7], [2, 1]])
for this_step in steps:
    result = (this_step, count_trees(input_grid, this_step))
    print(result)
    trees.append(result[1])
print(np.array(trees).prod())