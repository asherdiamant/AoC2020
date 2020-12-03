import numpy as np

expense = np.loadtxt('data/day1a.txt', dtype=int)
pairs = np.array(np.meshgrid(expense, expense)).T.reshape(-1, 2)
entries = pairs[pairs.sum(axis=1)==2020][0]
print(entries.prod())