import os

class AOC():
    def __init__(self, filename: str):
        self.filename = os.path.join('input', filename)
        print(os.getcwd())
        with open(self.filename) as f:
            self.lines = f.readlines()

    @property
    def as_string(self):
        return [item.strip('\n') for item in self.lines]

    @property
    def as_int(self):
        return [int(item) for item in self.lines]

    @property
    def group_by_double_newline(self):
        result = []
        group = []
        for line in self.as_string:
            if line == '':
                result.append(group)
                group = []
            else:
                group.append(line)
        result.append(group)
        return result

