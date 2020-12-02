from collections import namedtuple

data = AOC('2.txt').as_string

Case = namedtuple('Case', ['min', 'max', 'letter', 'password'])

inp = []

for line in data:
    line = line.split()
    least, most = line[0].split('-')
    inp.append(Case(int(least), int(most), line[1][0], line[2]))

valid = 0

for case in inp:
    if case.min <= case.password.count(case.letter) <= case.max:
            valid += 1

print(f'Part one: {valid}')
