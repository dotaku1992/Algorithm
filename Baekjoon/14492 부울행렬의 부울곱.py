#pypy3로 제출
n = int(input())
a = [list(map(int, input().split())) for _ in range(n)]
b = [list(map(int, input().split())) for _ in range(n)]
c = [[0 for _ in range(n)] for _ in range(n)]

ans = 0

for y in range(n):
    for x in range(n):
        for idx in range(n):
            c[y][x] |= a[y][idx] & b[idx][x]
        ans += c[y][x]

print(ans)
