from collections import defaultdict

group_count = 0
group_members = 0
answers = defaultdict(int)
customs_forms = []

with open('data/day6.txt') as f:
    for line in f.readlines()+['\n']:
        if line == '\n':
            group_count += 1
            customs_forms.append((group_count, group_members, len(answers.keys()), answers))
            answers = defaultdict(int)
        else:
            print(line)
            group_members += 1
            for c in line.rstrip():
                answers[c] += 1
            print(answers)
print('Total unique yes answers:', sum(form[2] for form in customs_forms))
