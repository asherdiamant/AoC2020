
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


mem = {}

with open('data/day14.txt') as f:
    for line in f.readlines():
        mp = re.match(r"mask = (?P<bin_str>[01X]+)$", line.strip())
        if mp:
            or_mask = int(mp['bin_str'].replace('X', '0'), 2)
            xs = [m.start() for m in re.finditer('X', mp['bin_str'])]
            mask_list = []
            for comb in range(2 ** len(xs)):
                bin_format = list(bin(comb)[2:].zfill(len(xs)))
                mask_str = list(mp['bin_str'])
                for loc, i in enumerate(xs):
                    mask_str[i] = bin_format[loc]
                mask_list.append(int(''.join(mask_str), 2) | or_mask)
        else:
            mp = re.match(r"mem\[(?P<loc>\d+)\] = (?P<value>\d+)", line.strip())
            if xs:
                address = int(mp['loc']) | or_mask
                address_str = list(bin(address)[2:].zfill(36))
                mem_locs = []
                for comb in range(2 ** len(xs)):
                    bin_format = list(bin(comb)[2:].zfill(len(xs)))
                    for loc, i in enumerate(xs):
                        address_str[i] = bin_format[loc]
                    mem_locs.append(int(''.join(address_str), 2))
                mem.update(dict.fromkeys(mem_locs, int(mp['value'])))
            else:
                mem[int(mp['loc'])] = int(mp['value'])


print('Sum of all values:', sum(mem.values()))