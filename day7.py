import re
from collections import defaultdict


class Bag:

    def __init__(self, spec_string):
        name = ""
        self.contains = {}
        self.spec = spec_string.replace('contain', ',').strip().split(',')
        self.name = " ".join(self.spec[0].split()[:-1])
        contents = self.spec[1:]
        if contents[0].strip() == 'no other bags.':
            self.contains = {}
        else:
            for bag_type in contents:
                pm = re.match(r'(?P<quantity>\d+)\s(?P<adj>\w+)\s(?P<color>\w+)', bag_type.strip())
                self.contains[pm['adj'] + ' ' + pm['color']] = int(pm['quantity'])

    def __repr__(self):
        return f'{self.name}, {self.contains}'


all_bags = {}
with open('data/day7.txt', 'r') as f:
    for line in f.readlines():
        current_bag = Bag(line)
        all_bags[current_bag.name] = current_bag

contained_by = defaultdict(list)
for bag in all_bags:
    for containing_bag, content in all_bags.items():
        if bag in content.contains.keys():
            contained_by[bag].append(containing_bag)


containers = set()
curr_level = ['shiny gold']
next_level = []
while len(curr_level) > 0:
    for bag in curr_level:
        for parent in contained_by[bag]:
            containers.add(parent)
            next_level.append(parent)
        curr_level = next_level
    next_level = []

print('\n'.join(containers))
print(f"Total of {len(containers)} bags")