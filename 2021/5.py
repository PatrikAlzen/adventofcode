from aocbase import AOC
from collections import Counter

data = AOC('5.txt').as_string
data = [[v.split(',') for v in vector.split(' -> ')] for vector in data]

points = []

for vector in data:
    x1 = int(vector[0][0])
    x2 = int(vector[1][0])
    y1 = int(vector[0][1])
    y2 = int(vector[1][1])
    if x1 == x2 or y1 == y2:
        for x in range(min(x1, x2), max(x1, x2) + 1):
            for y in range(min(y1, y2), max(y1, y2) + 1):
                points.append((x,y))

print(f'Part 1: {len([item for item in Counter(points).items() if item[1] > 1])}')

points = []

for vector in data:
    x1 = int(vector[0][0])
    x2 = int(vector[1][0])
    y1 = int(vector[0][1])
    y2 = int(vector[1][1])

    dx = 1 if x1 < x2 else -1
    dy = 1 if y1 < y2 else -1
    dx = 0 if x1 == x2 else dx
    dy = 0 if y1 == y2 else dy

    points.append((x1, y1))
    while x1 != x2 or y1 != y2:
        x1 += dx
        y1 += dy
        points.append((x1, y1))

print(f'Part 2: {len([item for item in Counter(points).items() if item[1] > 1])}')
