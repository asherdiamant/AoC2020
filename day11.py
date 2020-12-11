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


def is_outside(array, point):
    point_array = np.array(point)
    if (point_array < 0).any() or (point_array >= array.shape).any():
        return True
    return False


def calculate_visibles(array, pov):
    visibles = []
    for direction in [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]:
        curr = np.array(pov)
        while 1:
            if is_outside(array, curr + direction):
                break
            curr += direction
            if array[tuple(curr)]:
                visibles.append(tuple(curr))
                break
    return visibles


# create an array of lists of visible seats from each seat
visibility = np.empty(seat_map.shape, dtype=list)
for i in range(seat_map.shape[0]):
    for j in range(seat_map.shape[1]):
        visibility[i, j] = calculate_visibles(seat_map, (i, j))


def neighbors(array):
    result = np.zeros(array.shape)
    for x in range(array.shape[0]):
        for y in range(array.shape[1]):
            result[x, y] = sum([array[spot] for spot in visibility[x, y]])
    return result


curr_seats = np.zeros(seat_map.shape, dtype=int)
gen = 0
while 1:
    gen += 1
    neighbor_count = neighbors(curr_seats) * seat_map
    filling_seats = (neighbor_count == 0) * seat_map
    emptying_seats = neighbor_count >= 5
    next_seats = ((curr_seats | filling_seats) & ~emptying_seats)
    if (next_seats == curr_seats).all():
        print(f"Stable after {gen} generations. {next_seats.sum()} seats occupied")
        break

    curr_seats = next_seats
