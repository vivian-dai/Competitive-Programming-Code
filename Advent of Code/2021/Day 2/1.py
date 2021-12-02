with open("Advent of Code/2021/Day 2/input.txt") as inp:
    content = inp.read().splitlines()
    hor = 0
    ver = 0
    for line in content:
        command, val = line.split(" ")[0], int(line.split(" ")[1])
        if command == "forward":
            hor += val
        elif command == "down":
            ver += val
        elif command == "up":
            ver -= val
    print(hor*ver)