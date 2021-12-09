from aocbase import AOC

data = AOC('8.txt').as_string


occurences = 0
for line in data:
    _, output = line.split(' | ')
    output = [digit for digit in output.split()]
    for digit in output:
        if len(digit) in [2, 3, 4, 7]:
            occurences += 1

print(f'Part 1: {occurences}')

def decode(signal):
    mapping = {}

    while len(mapping) < 10:
        for x in signal.difference(mapping.values()):
            if len(x) == 2:
                mapping[1] = x
            elif len(x) == 3:
                mapping[7] = x
            elif len(x) == 4:
                mapping[4] = x
            elif len(x) == 7:
                mapping[8] = x
            elif len(x) == 6 and 4 in mapping and mapping[4].issubset(x):
                mapping[9] = x
            elif len(x) == 5 and 1 in mapping and mapping[1].issubset(x):
                mapping[3] = x
            elif len(x) == 6 and 7 in mapping and 9 in mapping and mapping[7].issubset(x) and mapping[9] != x:
                mapping[0] = x
            elif len(x) == 6 and 8 in mapping and 1 in mapping and x.issubset(mapping[8]) and not mapping[1].issubset(x):
                mapping[6] = x
            elif len(x) == 5 and 6 in mapping and x.issubset(mapping[6]):
                mapping[5] = x
            elif len(x) == 5 and 3 in mapping and 5 in mapping:
                mapping[2] = x
    return {value: key for key, value in mapping.items()}

def parse(signal, output):
    mapping = decode(signal)
    digit_string = ''
    for output_digit in output:
        digit_string += str(mapping[output_digit])
    return int(digit_string)


total = 0

for line in data:
    signal, output = line.split(' | ')
    signal = {frozenset(digit) for digit in signal.split()}
    output = [frozenset(digit) for digit in output.split()]
    total += parse(signal, output)

print(f'Part 2: {total}')

