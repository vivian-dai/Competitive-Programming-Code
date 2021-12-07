with open("Advent of Code/2021/Day 6/input.txt") as inp:
    fish = list(map(int, inp.read().split(",")))
    for i in range(80):
        end = len(fish)
        for j in range(end):
            if fish[j] == 0:
                fish[j] = 6
                fish.append(8)
            else:
                fish[j] -= 1
    print(len(fish))