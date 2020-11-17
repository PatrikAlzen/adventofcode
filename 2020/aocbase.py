import os

class AOC():
    def __init__(self, filename: str):
        self.filename = filename
        print(os.getcwd())
        with open(self.filename) as f:
            self.lines = f.readlines()

    @property
    def input_as_string(self):
        return [item.strip('\n') for item in self.lines]
    
    @property
    def input_as_int(self):
        return [int(item) for item in self.lines]

