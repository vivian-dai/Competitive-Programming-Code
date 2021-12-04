with open("Advent of Code/2021/Day 3/input.txt") as inp:
    content = inp.read().splitlines()
    oxygen = []
    co2 = []
    new_oxygen = []
    new_co2 = []
    for line in content:
        oxygen.append(line)
        co2.append(line)
    for i in range(len(content[0])):
        if len(oxygen) == 1:
            break
        one_count = 0
        zero_count = 0
        for o in oxygen:
            if o[i] == "1":
                one_count += 1
            else:
                zero_count += 1
        if zero_count > one_count:
            for o in oxygen:
                if o[i] == "0":
                    new_oxygen.append(o)
        else:
            for o in oxygen:
                if o[i] == "1":
                    new_oxygen.append(o)
        oxygen = new_oxygen
        new_oxygen = []

    for i in range(len(content[0])):
        if len(co2) == 1:
            break
        one_count = 0
        zero_count = 0
        for o in co2:
            if o[i] == "1":
                one_count += 1
            else:
                zero_count += 1
        if zero_count > one_count:
            for o in co2:
                if o[i] == "1":
                    new_co2.append(o)
        else:
            for o in co2:
                if o[i] == "0":
                    new_co2.append(o)
        co2 = new_co2
        new_co2 = []
    print(int(oxygen[0], 2)*int(co2[0], 2))