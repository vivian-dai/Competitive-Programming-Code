def base_convert(b):
    ret = ""
    if b[0] >= 'A' and b[0] <= 'Z':
        a = 0
        ind = len(b) - 1
        for c in b:
            a += (ord(c) - ord('A') + 1)*pow(26, ind)
            ind -= 1
        ret = str(a)
    else:
        b = int(b)
        while b > 0:
            if b%26 == 0:
                ret = 'Z' + ret
                b -= 1
            else:
                ret = chr(ord('A') + (b%26 - 1)) + ret
            b //= 26
    return ret

n = int(input())
for i in range(n):
    s = input()
    if s[0] == 'R':
        ind = 0
        for ind in range(len(s)):
            if s[ind].isdigit():
                break
        if 'C' in s and s.index('C') > ind:
            nums = s[1::].split("C")
            print(f"{base_convert(nums[1])}{nums[0]}")
        else:
            r, c = None, None
            for i in range(len(s)):
                if s[i].isdigit():
                    r = s[i::]
                    c = s[0:i]
                    print(f"R{r}C{base_convert(c)}")
                    break
    else:
        r, c = None, None
        for i in range(len(s)):
            if s[i].isdigit():
                r = s[i::]
                c = s[0:i]
                print(f"R{r}C{base_convert(c)}")
                break