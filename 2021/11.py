from aocbase import AOC
from itertools import product

data = AOC('11.txt').as_string

def neighbours(map, point):
    x, y = point
    return [(x+i, y+j) for i, j in product([1, 0, -1], repeat=2) if (x+i, y+j) != point and (x+i, y+j) in map.keys()]


def solve(data, part_one):
    total_flashes = 0

    evolutions = 100 if part_one else 1000

    map = {}

    for y in range(len(data)):
        for x in range(len(data[y])):
            map[(x, y)] = int(data[y][x])

    for step in range(evolutions):
        if not part_one: 
            if all([True if value == 0 else False for value in map.values()]):
                return step
        for key in map.keys():
            map[key] +=1
        flashed = set()
        while True:
            for key in map.keys():
                if map[key] > 9 and key not in flashed:
                    map[key] = 0
                    total_flashes +=1
                    flashed.add(key)
                    for key in neighbours(map, key):
                        if key not in flashed:
                            map[key] += 1
            if not[value for value in map.values() if value > 9]:
                break
    return total_flashes

print(f'Part 1: {solve(data, True)}')
print(f'Part 2: {solve(data, False)}')