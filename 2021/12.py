from aocbase import AOC
from collections import defaultdict, deque

data = AOC('12.txt').as_string

graph = defaultdict(list)

for line in data:
    a, b = line.strip().split('-')
    graph[a].append(b)
    graph[b].append(a)

print(graph)



def solve(graph, part_one):
    answer = 0
    queue = deque([])
    queue.append(('start', set(['start']), None))

    while queue:
        position, is_small, visited_twice = queue.popleft()
        if position == 'end':
            answer += 1
            continue
        for i in graph[position]:
            if not i in is_small:
                new = set(is_small)
                if i.islower():
                    new.add(i)
                queue.append((i, new, visited_twice))
            elif i in is_small and not visited_twice and i not in ['start', 'end'] and not part_one:
                queue.append((i, is_small, i))
    return answer

print(f'Part 1: {solve(graph, True)}')
print(f'Part 2: {solve(graph, False)}')
