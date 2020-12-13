from aocbase import AOC
from math import ceil, inf

data = AOC('13.txt').as_string

arrival_timestamp = int(data[0])
raw_departures = data[1].split(',')
departures = [int(x) for x in raw_departures if x != 'x']


def part_one():
    shortest_wait = inf
    best_departure = None

    for departure in departures:
        n = ceil(arrival_timestamp / departure)
        wait_time = n * departure - arrival_timestamp

        if wait_time < shortest_wait:
            shortest_wait = wait_time
            best_departure = departure

    return best_departure * shortest_wait

print(f'Part one: {part_one()}')

