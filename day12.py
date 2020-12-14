import numpy as np

directions = {'N': np.array([0, 1]), 'E': np.array([1, 0]), 'S': np.array([0, -1]), 'W': np.array([-1, 0])}


def rotation(point_to, direction, degrees):
    rads = np.deg2rad(degrees)
    if direction == 'L':
        rot_mat = np.array([[np.cos(rads), -np.sin(rads)],
                   [np.sin(rads), np.cos(rads)]])
    else:
        rot_mat = np.array([[np.cos(rads), np.sin(rads)],
                   [-np.sin(rads), np.cos(rads)]])
    return np.round(np.dot(rot_mat, point_to), 0).astype(int)


curr = np.array([0, 0])
facing = np.array([1, 0])

with open('data/day12.txt') as f:
    for line in f.readlines():
        opcode = line[0]
        param = int(line[1:].strip())
        if opcode in (directions.keys()):
            curr += directions[opcode] * param
        elif opcode in ['L', 'R']:
            facing = rotation(facing, opcode, param)
        elif opcode == 'F':
            curr += facing * param
        else:
            print("Unknown opcode:", opcode)
            break
    print("Manhattan distance is:", np.absolute(curr).sum())


ship = np.array([0, 0])
waypoint = np.array([10, 1])

with open('data/day12.txt') as f:
    for line in f.readlines():
        opcode = line[0]
        param = int(line[1:].strip())
        if opcode in (directions.keys()):
            waypoint += directions[opcode] * param
        elif opcode in ['L', 'R']:
            waypoint = rotation(waypoint, opcode, param)
        elif opcode == 'F':
            ship += waypoint * param
        else:
            print("Unknown opcode:", opcode)
            break
    print("Manhattan distance is:", np.absolute(ship).sum())