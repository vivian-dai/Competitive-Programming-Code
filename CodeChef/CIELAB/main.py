a, b = list(map(int, input().split(" ")))
if a - b == 1:
    print(2)
elif (a - b) % 10 == 0:
    print(a - b + 1)
else:
    print(a - b - 1)
