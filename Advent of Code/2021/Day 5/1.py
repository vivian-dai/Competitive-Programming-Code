with open("Advent of Code/2021/Day 5/input.txt") as inp:
    content = inp.read().splitlines()
    floor = []
    for i in range(1000):
        line = []
        for j in range(1000):
            line.append(0)
        floor.append(line)
    for command in content:
        p1, p2 = command.split(" -> ")[0], command.split(" -> ")[1]
        x1, y1 = int(p1.split(",")[0]), int(p1.split(",")[1])
        x2, y2 = int(p2.split(",")[0]), int(p2.split(",")[1])
        if x1 == x2:
            for i in range(min(y1, y2), max(y1, y2) + 1):
                floor[i][x1] += 1
        if y1 == y2:
            for i in range(min(x1, x2), max(x1, x2) + 1):
                floor[y1][i] += 1
    total = 0
    for i in range(len(floor)):
        for j in range(len(floor[0])):
            if floor[i][j] >= 2:
                total += 1
    print(total)
    