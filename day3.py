import numpy as np
from collections import Counter

grid = np.loadtxt('data/day3.txt', comments=None, dtype=np.str).reshape(-1, 1)
step = np.array([1, 3])
slope = step[1]/step[0]

traverse = slope * grid.shape[0]
repeats = int(traverse/len(grid[0]))
full_grid = np.tile(grid, (1, repeats+1))
full_grid = np.array([''.join(row) for row in full_grid])

route = [full_grid[0][0]]
for i in range(1, full_grid.shape[0]):
    next_element = i*step
    route.append(full_grid[next_element[0]][next_element[1]])

print(Counter(route))
