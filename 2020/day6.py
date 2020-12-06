from aocbase import AOC

data = AOC('6.txt').group_by_double_newline

inputs = []
total_answered = 0
total_unique = 0

for group in data:
    answered = set()
    for person in group:
        for answer in person:
            answered.add(answer)
    for question in answered:
        if len([person for person in group if question in person]) == len(group):
            total_unique += 1
    total_answered += len(answered)

print(f'Part one: {total_answered}')
print(f'Part two: {total_unique}')

