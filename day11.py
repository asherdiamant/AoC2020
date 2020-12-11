import numpy as np
from scipy.signal import convolve2d

seats = []
with open('data/day11.txt', 'r') as f:
    for line in f.readlines():
        seats.append([1 if seat == 'L' else 0 for seat in list(line.strip()) ])
seat_map = np.array(seats, dtype=bool) # available seats are 1, floor is 0

neighbors = [[1, 1, 1], [1, 0, 1], [1, 1, 1]] # count all neighbors but not the seat itself

curr_seats = np.zeros(seat_map.shape, dtype=int)

gen = 0

while 1:
    gen += 1
    neighbor_count = convolve2d(curr_seats, neighbors, mode='same', boundary='fill') * seat_map
    filling_seats = (neighbor_count == 0) * seat_map
    emptying_seats = neighbor_count >= 4
    next_seats = ((curr_seats | filling_seats) & ~emptying_seats)
    if (next_seats == curr_seats).all():
        print(f"Stable after {gen} generations. {next_seats.sum()} seats occupied")
        break

    curr_seats = next_seats
