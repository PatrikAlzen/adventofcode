from aocbase import AOC
from statistics import median

data = AOC('10.txt').as_string

closing = {']': '[', ')': '(', '}': '{', '>': '<'}
scoring = {')': 3, ']': 57, '}': 1197, '>': 25137}
mismatches = []


for line in data:
    chunks = []
    for symbol in line:
        if symbol in closing.values():
            chunks.append(symbol)
        elif symbol in closing.keys():
            if chunks[-1] == closing[symbol]:
                chunks.pop()
            else:
                mismatches.append(symbol)
                break

print(f'Part 1: {sum([scoring[m] for m in mismatches])}')

scores = []
scoring = {'(': 1,
           '[': 2,
           '{': 3,
           '<': 4}

for line in data:
    chunks = []
    error = False
    for symbol in line:
        if symbol in closing.values():
            chunks.append(symbol)
        elif symbol in closing.keys():
            if chunks[-1] == closing[symbol]:
                chunks.pop()
            else:
                error = True
                break
    if not error:
        score = 0
        chunks.reverse()
        for chunk in chunks:
            score *= 5
            score += scoring[chunk]
        scores.append(score)

print(f'Part 2: {median(scores)}')