import re
from collections import Counter


def is_valid(pw_entry):
    pm = re.match(r'(?P<minreps>\d+)-(?P<maxreps>\d+) (?P<repchar>.): (?P<pattern>\w+)', pw_entry.rstrip())
    c = Counter(pm['pattern'])
    reps = c[pm['repchar']]
    return int(pm['minreps']) <= reps <= int(pm['maxreps'])


def is_valid2(pw_entry):
    pm = re.match(r'(?P<first>\d+)-(?P<second>\d+) (?P<testchar>.): (?P<pattern>\w+)', pw_entry.rstrip())
    first_loc = int(pm['first']) - 1
    second_loc = int(pm['second']) - 1
    return(pm['testchar']==pm['pattern'][first_loc]) != (pm['testchar']==pm['pattern'][second_loc])


with open('data/day2.txt', 'r') as f:
    password_db = f.readlines()

valid_pws = [is_valid(x) for x in password_db]
print(sum(valid_pws))

valid_pws2 = [is_valid2(x) for x in password_db]
print(sum(valid_pws2))