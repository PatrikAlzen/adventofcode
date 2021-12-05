from aocbase import AOC

data = AOC('3.txt').as_string
length = len(data[0])

foo = [[0, 0] for _ in range(length)]
for line in data:
    for i in range(length):
        if line[i] == '0':
            foo[i][0] += 1
        elif line[i] == '1':
            foo[i][1] += 1

gamma = ''
epsilon = ''

for i in range(length):
    if foo[i][0] > foo[i][1]:
        gamma += '0'
        epsilon += '1'
    else:
        gamma += '1'
        epsilon += '0'

print(f'Part 1: {int(gamma, 2) * int(epsilon, 2)}')

from collections import Counter

def get_rating(data, bit_criteria: bool):
    for i in range(len(data[0])):
        count = Counter(line[i] for line in data)
        if bit_criteria:
            target = 1 if count['1'] >= count['0'] else 0
        else:
            target = 0 if count['1'] >= count['0'] else 1

        data = [line for line in data if line[i] == str(target)]

        if len(data) == 1:
            return data[0]

print(f'Part 2: {int(get_rating(data, True), 2) * int(get_rating(data, False), 2)}')