n, m = map(int, input().split())
arr = [[0 for _ in range(100)] for _ in range(100)]
for _ in range(n):
    ldx, ldy, rux, ruy = map(int, input().split())
    for y in range(ldy - 1, ruy):
        for x in range(ldx - 1, rux):
            arr[y][x] += 1

ans = 0
for y in range(100):
    for x in range(100):
        ans += (arr[y][x] > m)

print(ans)
