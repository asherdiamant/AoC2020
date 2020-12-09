import numpy as np


def calc_all_sums(array, pairs_list, shift):
    all_sums = []
    for pair in pairs_list:
        all_sums.append(array[pair[0]+shift] + array[pair[1]+shift])
    return set(all_sums)


cyphertext = np.loadtxt('data/day9.txt', dtype=int)
indices = range(25)
#    preamble = cyphertext[i-25:i]
pairs = np.array(np.meshgrid(indices, indices)).T.reshape(-1, 2)
#    all_sums = pairs.sum(axis=1)

valid_pairs = [pair for pair in pairs if pair[0] != pair[1]]

for i in range(len(cyphertext)-25):
    curr_value = cyphertext[i+25]
    valid_sums = calc_all_sums(cyphertext, valid_pairs, i)
    if curr_value not in valid_sums:
        print(f"{i+25}: {curr_value} not valid.")
        break
