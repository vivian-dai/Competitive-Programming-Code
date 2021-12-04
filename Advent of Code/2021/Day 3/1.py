with open("Advent of Code/2021/Day 3/input.txt") as inp:
    content = inp.read().splitlines()
    one_count = []
    zero_count = []
    for char in content[0]:
        if char == "1":
            one_count.append(1)
            zero_count.append(0)
        elif char == "0":
            one_count.append(0)
            zero_count.append(1)
    for line in content:
        for i in range(len(line)):
            if line[i] == "1":
                one_count[i] += 1
            else:
                zero_count[i] += 1
    gamma = 0
    epsilon = 0
    print(zero_count, one_count)
    for i in range(len(zero_count)):
        if one_count[i] > zero_count[i]:
            gamma += 2**(len(zero_count) - i - 1)
        else:
            epsilon += 2**(len(zero_count) - i - 1)
    print(gamma*epsilon)