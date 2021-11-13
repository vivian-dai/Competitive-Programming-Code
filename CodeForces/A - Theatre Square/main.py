n, m, a = list(map(int, input().split(" ")))

side1 = n//a

if n%a != 0:
    side1 += 1

side2 = m//a
if m%a != 0:
    side2 += 1

print(side1*side2)