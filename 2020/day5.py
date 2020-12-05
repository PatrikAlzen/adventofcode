from aocbase import AOC

data = AOC("2020/5.txt").as_string


def seat_id(row, column):
    return row * 8 + column


def binary_partition(data, lower, upper):
    for item in data:
        difference = int((upper - lower) / 2) + 1
        if item in ["F", "L"]:
            upper = upper - difference
            result = lower
        elif item in ["B", "R"]:
            lower = lower + difference
            result = upper
    return result


def process_boarding_pass(boarding_pass):
    row = binary_partition(boarding_pass[:7], 0, 127)
    column = binary_partition(boarding_pass[7:], 0, 7)
    return {"row": row, "column": column, "id": seat_id(row, column)}


def process_all(data):
    result = []
    for bp in data:
        result.append(process_boarding_pass(bp))
    return result


seat_ids = [bp["id"] for bp in process_all(data)]

print(f"Part one: {max(seat_ids)}")

for seat_id in range(min(seat_ids), max(seat_ids)):
    if seat_id not in seat_ids and seat_id - 1 in seat_ids and seat_id + 1 in seat_ids:
        print(f"Part two: {seat_id}")
