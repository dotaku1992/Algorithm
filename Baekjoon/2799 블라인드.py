n, m = map(int, input().split())

apt = [input() for _ in range(n + 4 * n + 1)]
ans = [0, 0, 0, 0, 0]
for y in range(n):
    for x in range(m):
        floor = 0
        ny, nx = 4 * y + 1 * (y + 1), 4 * x + 1 * (x + 1)

        for plus in range(4):
            if apt[ny + plus][nx] == '*':
                floor += 1
        ans[floor] += 1
print(*ans)
