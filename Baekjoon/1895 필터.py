n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
benchmark = int(input())
ans = 0
for y in range(n - 3 + 1):
    for x in range(m - 3 + 1):
        subarr = [arr[yidx][xidx] for yidx in range(y, y + 3) for xidx in range(x, x + 3)]
        subarr.sort()
        ans += (subarr[4] >= benchmark)
print(ans)
