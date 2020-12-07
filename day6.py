import numpy as np
from collections import defaultdict


group_count = 0
group_members = 0
answers = defaultdict(int)
customs_forms = []

with open('data/day6.txt') as f:
    for line in f.readlines()+['\n']:
        if line == '\n':
            group_count += 1
            customs_forms.append((group_count, group_members, answers))
            answers = defaultdict(int)
            group_members = 0
        else:
            group_members += 1
            for c in line.rstrip():
                answers[c] += 1

print('Total unique yes answers: ', sum(len(form[2]) for form in customs_forms))

print('Total unanimous yes answers: ', sum(sum(np.array(list(form[2].values())) == form[1]) for form in customs_forms))