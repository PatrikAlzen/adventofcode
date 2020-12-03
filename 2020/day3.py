from aocbase import AOC
from collections import namedtuple

data = AOC('3.txt').as_string

point = namedtuple('Point', ['x', 'y'])

def count_hits(intervals, data):
    total = 1
    for interval in intervals:
        hits = 0
        current = point(interval[0], interval[1])
        width = len(data[current.y])
        while current.y < len(data):
            if data[current.y][current.x % width] == '#':
                hits += 1
            current = point(current.x + interval[0], current.y + interval[1])
        total = total * hits
    return total

print(f'Part one: {count_hits([(3, 1)], data)}')
print(f'Part two: {count_hits([(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)], data)}')
