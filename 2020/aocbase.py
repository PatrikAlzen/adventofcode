import os
import time


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


def timeit(func):
    def timed(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        if 'log_time' in kwargs:
            name = kwargs.get('log_name', func.__name__.upper())
            kwargs['log_time'][name] = int((end_time - start_time) * 1000)
        else:
            print(f'{func.__name__}  {(end_time - start_time) * 1000:.2f} ms')
        return result

    return timed
