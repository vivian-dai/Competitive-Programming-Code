with open("Advent of Code/2021/Day 6/input.txt") as inp:
    fish = list(map(int, inp.read().split(",")))
    fishes = [0, 0, 0, 0, 0, 0, 0, 0, 0]
    for f in fish:
        fishes[f] += 1
    for i in range(256):
        zero_count = fishes[0]
        # print(fishes, zero_count)
        for j in range(1, len(fishes)):
            fishes[j - 1] = fishes[j]
        fishes[8] = 0
        fishes[8] += zero_count
        fishes[6] += zero_count
    total = 0
    for f in fishes:
        total += f
    print(total)