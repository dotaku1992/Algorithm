isobserved = [0] * 11
initpos = [0] * 11
n = int(input())

ans = 0
for _ in range(n):
    cowidx, dir = map(int, input().split())
    if not isobserved[cowidx]:
        isobserved[cowidx] = 1
        initpos[cowidx] = dir
    else:
        ans += (initpos[cowidx] != dir)
        initpos[cowidx] = dir
print(ans)
