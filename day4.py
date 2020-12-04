import re

passport_validity = []
required_fields = ['byr', 'ecl', 'eyr', 'hcl', 'hgt', 'iyr', 'pid']
required_fields.sort()
optional_fields = ['cid']


def is_valid(passport):
    p_keys = list(passport.keys())
    try:
        p_keys.remove('cid')
    except ValueError:
        pass
    p_keys.sort()

    return p_keys == required_fields



def parse_line(in_line):
    dic = {}
    for field in in_line.split():
        mp = re.match('(?P<name>.+):(?P<value>.+)', field)
        dic[mp['name']] = mp['value']
    return dic


passport = {}
with open('data/day4.txt', 'r') as f:
    for line in f.readlines() + ['\n']:
        if line == '\n':
            passport_validity.append(is_valid(passport))
            print(passport, is_valid(passport))
            passport = {}
        else:
            temp_dic = parse_line(line)
            passport.update(temp_dic)
print(f'{sum(passport_validity)} valid passports')
