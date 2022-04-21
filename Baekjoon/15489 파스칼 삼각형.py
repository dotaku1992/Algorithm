import math

r, c, w = map(int, input().split())
ans = 0
for y in range(w):
    for x in range(0, y + 1):
        ans += math.comb(r - 1 + y, c - 1 + x)

print(ans)
