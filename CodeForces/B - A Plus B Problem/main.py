n, q = list(map(int, input().split(" ")))
rows = []
rows.append(input())
rows.append(input())
rows.append(int(rows[0]) + int(rows[1]))

def number_changed(original, after):
    total = 0
    og_str = str(original)
    aft_str = str(after)
    if len(og_str) == len(aft_str):
        for i in range(len(og_str)):
            if og_str[i] != aft_str[i]:
                total += 1
        return total
    elif len(og_str) > len(aft_str):
        diff = len(og_str) - len(aft_str)
        for i in range(len(aft_str)):
            if og_str[i + diff] != aft_str[i]:
                total += 1
        return total + diff
    else:
        diff = len(aft_str) - len(og_str)
        for i in range(len(og_str)):
            if og_str[i] != aft_str[i + diff]:
                total += 1
        return total + diff

def do_stuff():
    r, c, d = list(map(int, input().split(" ")))
    rows[r - 1] = rows[r - 1][:c - 1] + str(d) + rows[r - 1][c:]
    final = int(rows[0]) + int(rows[1])
    fin_str = str(final)
    thing = -1
    if len(fin_str) == n:
        thing = fin_str[c - 1]
    else:
        if c - 1 - (n - len(fin_str)) >= 0:
            thing = fin_str[c - 1 - (n - len(fin_str))]
        else:
            thing = 0
    print(thing, number_changed(rows[2], final) + 1)
    rows[2] = final

for i in range(q):
    do_stuff()