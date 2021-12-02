from typing import List
from aocbase import AOC

data = AOC('2.txt').as_string

depth = 0
horizontal_position = 0

class Sub:
    def __init__(self, data: List[str]) -> None:
        self.commands = [item.split(' ') for item in data]
        self.depth = 0
        self.horizontal_position = 0
        self.actions = {'up': self.up,
                        'down': self.down,
                        'forward': self.forward}
        self.process()
    
    def process(self):
        for command in self.commands:
            self.actions[command[0]](command[1])

    def up(self, n):
        self.depth -= int(n)
    
    def down(self, n):
        self.depth += int(n)

    def forward(self, n):
        self.horizontal_position += int(n)

    @property
    def position(self):
        return self.depth * self.horizontal_position


# Part 1
sub = Sub(data)
print(f'Part 1: {sub.position}')

# Part 2
class Sub:
    def __init__(self, data: List[str]) -> None:
        self.commands = [item.split(' ') for item in data]
        self.aim = 0
        self.depth = 0
        self.horizontal_position = 0
        self.actions = {'up': self.up,
                        'down': self.down,
                        'forward': self.forward}
        self.process()
    
    def process(self):
        for command in self.commands:
            self.actions[command[0]](command[1])

    def up(self, n):
        self.aim -= int(n)
    
    def down(self, n):
        self.aim += int(n)

    def forward(self, n):
        self.horizontal_position += int(n)
        self.depth += self.aim * int(n)

    @property
    def position(self):
        return self.depth * self.horizontal_position

sub = Sub(data)
print(f'Part 2: {sub.position}')
