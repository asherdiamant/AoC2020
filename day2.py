import re
from collections import Counter


def is_valid(pw_entry):
    pm = re.match(r'(?P<minreps>\d+)-(?P<maxreps>\d+) (?P<repchar>.): (?P<pattern>\w+)', pw_entry.rstrip())
    c = Counter(pm['pattern'])
    reps = c[pm['repchar']]
    return int(pm['minreps']) <= reps <= int(pm['maxreps'])


with open('data/day2.txt', 'r') as f:
    password_db = f.readlines()

valid_pws = [is_valid(x) for x in password_db]
print(sum(valid_pws))
