import re
from collections import defaultdict

rules = {}
my_ticket = []
nearby_tickets = []
with open('data/day16.txt') as f:
    line = f.readline()
    while line != '\n':
        mp = re.match(r"(?P<field_name>.+): (?P<min1>\d+)-(?P<max1>\d+) or (?P<min2>\d+)-(?P<max2>\d+)", line.strip())

        rules[mp['field_name']] = list(range(int(mp['min1']), int(mp['max1'])+1)) + \
                                  list(range(int(mp['min2']), int(mp['max2'])+1))
        line = f.readline()

    line = f.readline()
    line = f.readline()
    my_ticket = [int(x) for x in line.strip().split(',')]

    line = f.readline()
    line = f.readline()

    for line in f.readlines():
        nearby_tickets.append([int(x) for x in line.strip().split(',')])

all_valid_values = set()
for name, valid_values in rules.items():
    all_valid_values = all_valid_values.union(valid_values)


def is_valid_ticket(ticket, valids):
    invalid_values = [x for x in ticket if x not in valids]
    return invalid_values == [], invalid_values


nearby_validity = [is_valid_ticket(ticket, all_valid_values)[1] for ticket in nearby_tickets
                   if not is_valid_ticket(ticket, all_valid_values)[0]]

print("Ticket scanning error rate:", sum([sum(elem) for elem in nearby_validity]))

valid_tickets = [ticket for ticket in nearby_tickets if is_valid_ticket(ticket, all_valid_values)[0]]


# Part 2

values_by_location = defaultdict(list)
for ticket in valid_tickets:
    for loc, value in enumerate(ticket):
        values_by_location[loc].append(value)

possible_fields = defaultdict(list)
for field, vvalues in rules.items():
    for loc, actual_values in values_by_location.items():
        if all(elem in vvalues for elem in actual_values):
            possible_fields[loc].append(field)

final_fields = defaultdict(str)
change = 1
while change:
    change = 0
    this_pass = []
    for key, value in possible_fields.items():
        if len(value) == 1:
            this_pass.append((key, value))
    if this_pass:
        change = 1
        for key, value in this_pass:
            del(possible_fields[key])
            final_fields[key] = value[0]
            for loc, fields in possible_fields.items():
                if value[0] in fields:
                    possible_fields[loc].remove(value[0])

result = 1
for loc, field in final_fields.items():
    if field[0:9] == 'departure':
        result *= my_ticket[loc]
print(result)


