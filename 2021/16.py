from aocbase import AOC
import math

data = AOC('16.txt').as_string[0]

line = f'{int(data, 16):b}'.zfill(len(data * 4))


def process(bitstream):
    version = int(bitstream[:3], 2)
    type_id = int(bitstream[3:6], 2)

    # literal
    if type_id == 4:
        i = 6
        result = ''
        while True:
            result += bitstream[i+1:i+5]
            i += 5
            if bitstream[i-5] == '0':
                break
        return version, i, int(result, 2)

    # operator
    if bitstream[6] == '0':
        subpacket_length = int(bitstream[7:22], 2)
        i = 22
        numbers = []
        while i < subpacket_length + 22:
            v_sum, l, result = process(bitstream[i:])
            i += l
            version += v_sum
            numbers.append(result)

    else:
        num_subpackets = int(bitstream[7:18], 2)
        i = 18
        numbers = []
        for _ in range(num_subpackets):
            v_sum, l, result = process(bitstream[i:])
            version += v_sum
            i += l
            numbers.append(result)

    if type_id == 0:
        result = sum(numbers)
    elif type_id == 1:
        result = math.prod(numbers)
    elif type_id == 2:
        result = min(numbers)
    elif type_id == 3:
        result = max(numbers)
    elif type_id == 5:
        result = int(numbers[0] > numbers[1])
    elif type_id == 6:
        result = int(numbers[0] < numbers[1])
    elif type_id == 7:
        result = int(numbers[0] == numbers[1])
    return version, i, result


version_sum, _, value = process(line)

print(f'Part 1: {version_sum}')
print(f'Part 2: {value}')
