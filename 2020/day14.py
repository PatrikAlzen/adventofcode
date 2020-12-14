from aocbase import AOC, timeit
import re

data = AOC('14.txt').as_string


def apply_mask(mask, value):
    for index, bit in enumerate(mask):
        if bit in '01':
            value = value[:index] + bit + value[index+1:]
    return value


def part_one(data):
    memory = {}
    for line in data:
        if line.startswith('mask'):
            mask = line.split(' = ')[1]
        elif line.startswith('mem'):
            location, value = line.split(' = ')
            location = re.sub(r'[^0-9]+', '', location)
            value = f'{int(value):07b}'.zfill(36)
            memory[location] = apply_mask(mask, value)

    print(memory.items())
    return sum([int(x, 2) for x in memory.values()])

print(f'Part one: {part_one(data)}')
