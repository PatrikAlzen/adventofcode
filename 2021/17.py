target = [253, 280, -73,-46]

#target = [20, 30, -10, -5]

xs, xe, ys, ye = target




max_y = 0
solutions = set()

for DX in range(1, xe+1):
    for DY in range(ys, 100):
        x, y = 0, 0
        dx, dy = DX, DY
        local_max_y = 0
        for step in range(xe):
            x += dx
            y += dy
            if y > local_max_y:
                local_max_y = y
            dx = max(0, dx-1)
            dy -= 1
            if xs <= x <= xe and ys <= y <= ye:
                max_y = max(local_max_y, max_y)                    
                solutions.add((DX, DY))

            if y < ys:
                break

print(f'Part 1: {max_y}')
print(f'Part 2: {len(solutions)}')