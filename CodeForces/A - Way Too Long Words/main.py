def do_stuff():
    word = input()
    if len(word) > 10:
        print(word[0] + str(len(word) - 2) + word[-1])
    else:
        print(word)

n = int(input())
while n > 0:
    do_stuff()
    n -= 1