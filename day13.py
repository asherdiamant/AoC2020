from math import ceil

from numpy import argmin

with open('data/day13.txt') as f:
    min_time = int(f.readline().strip())
    bus_ids = [int(elem) for elem in f.readline().strip().split(',') if elem != 'x']

print("My minimum departure time:", min_time)
print("Active busses:", bus_ids)

dep_times = [ceil(min_time/x) * x for x in bus_ids]
best_bus = bus_ids[argmin(dep_times)]
wait_time = dep_times[argmin(dep_times)] - min_time
print("Best bus times wait time:", best_bus * wait_time)

