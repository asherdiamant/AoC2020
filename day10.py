import numpy as np
from collections import Counter
from math import factorial
from scipy.special import comb
from itertools import groupby

adapters = np.loadtxt('data/day10.txt', dtype=int)
adapters.sort()
adapters = np.append(adapters, max(adapters) + 3)
shifted_adapters = np.insert(adapters[:-1], 0, 0)
diffs = adapters - shifted_adapters
jolts = Counter(diffs)

print("1-jolts multiplied by 3-jolts combos:", jolts[1] * jolts[3])

