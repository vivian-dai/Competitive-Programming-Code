with open("Advent of Code/2021/Day 7/input.txt") as inp:
    content = list(map(int, inp.read().split(",")))
    min_fuel = 9999999999
    content.sort()
    min_val = content[0]
    max_val = content[-1]
    for i in range(min_val, max_val + 1):
        fuel = 0
        for num in content:
            n = abs(num - i)
            fuel += (n*(n + 1))/2
        if fuel < min_fuel:
            min_fuel = fuel
    print(int(min_fuel))