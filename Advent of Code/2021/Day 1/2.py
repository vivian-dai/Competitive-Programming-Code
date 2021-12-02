with open("Advent of Code/2021/Day 1/input.txt") as inp:
    content = list(map(int, inp.read().splitlines()))
    out = 0
    sum_1 = 0
    sum_2 = 0
    sum_1 = content[0] + content[1] + content[2]
    sum_2 = content[1] + content[2] + content[3]
    for i in range(4, len(content)):
        if sum_2 > sum_1:
            out += 1
        sum_1 += content[i - 1] - content[i - 4]
        sum_2 += content[i] - content[i - 3]

    if sum_2 > sum_1:
        out += 1
    print(out)