from aocbase import AOC

data = [int(n) for n in AOC('7.txt').lines[0].split(',')]

fuel = 9999999999999999999999999999999
for n in range(min(data), max(data) + 1):
    subtotal = 0
    for pos in data:
        diff = abs(pos - n)
        subtotal += diff
        if subtotal >= fuel:
            break
    fuel = min(subtotal, fuel)

print(f'Part 1: {fuel}')


fuel = 9999999999999999999999999999999
for n in range(min(data), max(data) + 1):
    subtotal = 0
    for pos in data:
        diff = abs(pos - n)
        subtotal += (diff * (diff + 1)) // 2
        if subtotal >= fuel:
            break
    fuel = min(subtotal, fuel)

print(f'Part 2: {fuel}')