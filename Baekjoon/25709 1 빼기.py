import sys

n = int(sys.stdin.readline().rstrip())
ans = 0
while n:
    strn = str(n)
    for idx, ele in enumerate(strn):
        if ele == '1':
            strn = strn[:idx] + strn[idx + 1:]
            if not strn:
                n = 0
            else:
                n = int(strn)
            break
    else:
        n -= 1
    ans += 1
print(ans)
