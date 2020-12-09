import numpy as np

cyphertext = np.loadtxt('data/day9.txt', dtype=int)
indices = range(25)
pairs = np.array(np.meshgrid(indices, indices)).T.reshape(-1, 2)
valid_pairs = [pair for pair in pairs if pair[0] != pair[1]]


def calc_all_sums(array, pairs_list, shift):
    all_sums = []
    for pair in pairs_list:
        all_sums.append(array[pair[0]+shift] + array[pair[1]+shift])
    return set(all_sums)

for i in range(len(cyphertext)-25):
    curr_value = cyphertext[i+25]
    valid_sums = calc_all_sums(cyphertext, valid_pairs, i)
    if curr_value not in valid_sums:
        first_invalid = curr_value
        print(f"{i+25}: {curr_value} not valid.")
        break


for start in range(len(cyphertext)-1):
    for length in range(2, len(cyphertext) - start):
        total = np.sum(cyphertext[start:start+length])
        if total > first_invalid:
            break
        if total == first_invalid:
            print(f"Sequence summing up to {first_invalid}: \n", "start:", start, "length:", length, cyphertext[start:start+length])
            smallest = np.min(cyphertext[start:start+length])
            largest = np.max(cyphertext[start:start+length])
            print(f"Found! {smallest} + {largest} = {smallest + largest}")
            exit(0)
print("Not found :(")

