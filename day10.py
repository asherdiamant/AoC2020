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

# If the difference is 3, we must keep both adapters
# When we have a run of difference 1 adapters, we can pick and choose which and how many to keep
# depending on the run length. We need at least run-3 adapters to make sure all gaps are 3 or less


def options(run):
    total = 0
    for i in range(max(run-3, 0), run):
        total += comb(run-1, i)
    return total


runs_of_one = [len(list(g)) for b, g in groupby(diffs) if b == 1]
print(int(np.prod([options(x) for x in runs_of_one])), "different combinations of adapters")