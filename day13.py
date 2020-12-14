from math import ceil

from numpy import argmin

with open('data/day13.txt') as f:
    min_time = int(f.readline().strip())
    cycle_times = f.readline().strip().split(',')
    bus_ids = [int(elem) for elem in cycle_times if elem != 'x']

print("My minimum departure time:", min_time)
print("Active busses:", bus_ids)

dep_times = [ceil(min_time/x) * x for x in bus_ids]
best_bus = bus_ids[argmin(dep_times)]
wait_time = dep_times[argmin(dep_times)] - min_time
print("Best bus times wait time:", best_bus * wait_time)


# This is a chinese remainder theoreme
# https://en.wikipedia.org/wiki/Chinese_remainder_theorem#Computation

offsets = {}
for i in range(len(cycle_times)):
    if cycle_times[i] != 'x':
        offsets[int(cycle_times[i])] = i

min_offsets = {cycle:offset % cycle for cycle, offset in offsets.items()}


from tqdm import tqdm

longest = max([min_offsets.keys()])
sorted_cycles = sorted(min_offsets.keys(), reverse=True)

curr_prduct = 1
departure = sorted_cycles[0] - min_offsets[sorted_cycles[0]]
for j in tqdm(range(len(sorted_cycles)-1)):
    cycle = sorted_cycles[j]
    next_cycle = sorted_cycles[j+1]
    offset = cycle - min_offsets[cycle]
    curr_prduct *= cycle
    while 1:
        departure += curr_prduct
        if departure % next_cycle == (next_cycle - min_offsets[next_cycle]) % next_cycle:
            print("Found:", departure, next_cycle, min_offsets[next_cycle])
            break
print(departure)