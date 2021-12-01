from aocbase import AOC

data = AOC('1.txt').as_int

# Part 1
print('Part 1: ', sum([1 for a, b in zip(data[0:-1], data[1:]) if a < b]))

# Part 2
sums = [a+b+c for a, b, c in zip(data[0:-2], data[1:-1], data[2:])]
print('Part 2: ', sum([1 for a, b in zip(sums[0:-1], sums[1:]) if a < b]))