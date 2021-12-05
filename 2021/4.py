with open('input/4.txt') as f:
    numbers = [int(n) for n in f.readline().split(',')]
    boards = []
    board = []

    for line in f.readlines():
        if line == '\n' and board != []:
            boards.append(board)
            board = []
        elif line != '\n':
            board.append([int(n) for n in line.split(' ') if n != ''])
    boards.append(board)

possible_wins = []

for board in boards:
    wins = []
    for i in range(len(board)):
        wins.append(board[i])
        wins.append([line[i] for line in board])
    possible_wins.append(wins)


drawn_numbers = []
won = []
first_done = False
for n in numbers:
    drawn_numbers.append(n)
    for i in range(len(boards)):
        for line in possible_wins[i]:
            if all([True if n in drawn_numbers else False for n in line]):
                if not first_done:
                    print(f'Part 1: {sum([n for line in boards[i] for n in line if n not in drawn_numbers]) * drawn_numbers[-1]}')
                    first_done = True
                if i not in won:
                    won.append(i)
                score = sum([n for line in boards[i] for n in line if n not in drawn_numbers]) * drawn_numbers[-1]
                if len(won) == len(boards): 
                    print(f'Part 2: {score}')
                    quit()
