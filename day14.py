
import re

mem = {}
or_mask = 0
and_mask = 2 ^ 36 - 1

with open('data/day14.txt') as f:
    for line in f.readlines():
        mp = re.match(r"mask = (?P<bin_str>[01X]+)$", line.strip())
        if mp:
            or_mask = int(mp['bin_str'].replace('X', '0'), 2)
            and_mask = int(mp['bin_str'].replace('X', '1'), 2)
        else:
            mp = re.match(r"mem\[(?P<loc>\d+)\] = (?P<value>\d+)", line.strip())
            mem[int(mp['loc'])] = int(mp['value']) & and_mask | or_mask

print('Sum of all values:', sum(mem.values()))