from aocbase import AOC
from itertools import permutations

data = AOC('1.txt')

combinations = permutations(data.as_int, 2)

for combo in combinations:
    if combo[0] + combo[1] == 2020:
        print(f'Part one: {combo[0] * combo[1]}')
        break

combinations = permutations(data.as_int, 3)

for combo in combinations:
    if combo[0] + combo[1] + combo[2] == 2020:
        print(f'Part two: {combo[0] * combo[1] * combo[2]}')
        break
