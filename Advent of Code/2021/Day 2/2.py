with open("Advent of Code/2021/Day 2/input.txt") as inp:
    content = inp.read().splitlines()
    hor = 0
    aim = 0
    dep = 0
    for line in content:
        command, val = line.split(" ")[0], int(line.split(" ")[1])
        if command == "forward":
            hor += val
            dep += aim*val
        elif command == "down":
            aim += val
        elif command == "up":
            aim -= val
    print(hor*dep)