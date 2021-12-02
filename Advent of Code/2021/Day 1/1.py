with open("Advent of Code/2021/Day 1/input.txt") as inp:
    content = list(map(int, inp.read().splitlines()))
    out = 0
    for i in range(1, len(content)):
        if content[i] > content[i - 1]:
            out += 1
    print(out)