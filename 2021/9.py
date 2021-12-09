from aocbase import AOC

data = AOC('9.txt').as_string

map = {}

for y in range(len(data)):
    for x in range(len(data[y])):
        map[(x, y)] = int(data[y][x])

def find_lowspots(map):
    lowspots = {}
    for x, y in map.keys():
        spot = map[(x, y)]
        surroundings = []
        
        surroundings.append(map.get((x+1, y), 9))
        surroundings.append(map.get((x-1, y), 9))
        surroundings.append(map.get((x, y+1), 9))
        surroundings.append(map.get((x, y-1), 9))

        if all([spot < place for place in surroundings]):
            lowspots[(x, y)] = spot
    return lowspots

lowspots = find_lowspots(map)

print(f'Part 1: {sum([value +1 for value in lowspots.values()])}')



def expand_basin(x, y):
    basin = {(x, y)}
    surroundings = [(x+1, y), (x-1, y), (x, y+1), (x, y-1)]

    for a, b in surroundings:
        if map.get((x, y), 9) < map.get((a, b), 9) < 9:
            basin |= expand_basin(a, b)
    return basin

basin_sizes = sorted([len(expand_basin(x, y)) for x, y in lowspots.keys()])
print("Part 2:", basin_sizes[-1] * basin_sizes[-2] * basin_sizes[-3])
