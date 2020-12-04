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

    if p_keys == required_fields:
        byr_valid = 1920 <= int(passport['byr']) <= 2002
        iyr_valid = 2010 <= int(passport['iyr']) <= 2020
        eyr_valid = 2020 <= int(passport['eyr']) <= 2030
        hgt = passport['hgt']
        hgt_valid = (hgt[-2:] == 'cm' and 150 <= int(hgt[:-2]) <= 193) or (hgt[-2:] == 'in' and 59 <= int(hgt[:-2]) <= 76)
        hcl_valid = (re.match('#[0-9|a-f]{6}', passport['hcl']) is not None)
        ecl_valid = passport['ecl'] in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']
        pid_valid = (re.match('^\d{9}$', passport['pid']) is not None)
        valid = byr_valid and iyr_valid and \
                eyr_valid and hgt_valid and hcl_valid and ecl_valid and pid_valid
    else:
        valid = False

    return valid


def parse_line(in_line):
    dic = {}
    for field in in_line.split():
        mp = re.match('(?P<name>.+):(?P<value>.+)', field)
        dic[mp['name']] = mp['value']
    return dic


passport = {}
i = 1
with open('data/day4.txt', 'r') as f:
    for line in f.readlines() + ['\n']:
        if line == '\n':
            passport_validity.append(is_valid(passport))
            if is_valid(passport):
                print(passport, len(passport.keys()))
            passport = {}
        else:
            temp_dic = parse_line(line)
            passport.update(temp_dic)
print(f'{sum(passport_validity)} valid passports')
