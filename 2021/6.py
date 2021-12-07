from aocbase import AOC
from collections import Counter

data = AOC('6.txt').lines[0]

def calc_fish(data, days):
    counter = Counter(data)
    occurences = [counter.get(i, 0) for i in range(9)]
    for _day in range(days):
        number_of_spawns = occurences[0]
        for i in range(8):
            occurences[i] = occurences[i+1]
        occurences[6] += number_of_spawns
        occurences[8] = number_of_spawns
    return sum(occurences)

print(f'Part 2: {calc_fish([int(n) for n in data.split(",")], 80)}')
print(f'Part 2: {calc_fish([int(n) for n in data.split(",")], 256)}')