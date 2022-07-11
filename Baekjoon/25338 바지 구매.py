import math


def func(a, b, c):
    Q = -b / (2 * a)
    R = math.sqrt(b * b - 4 * a * c) / (2 * a)
    x1, x2 = Q + R, Q - R
    return x1, x2


a, b, c, d = map(int, input().split())
n = int(input())
minh = d
maxh = c

ans = 0
for _ in range(n):
    u, v = map(int, input().split())
    if minh <= u <= maxh:
        x1, x2 = func(a, -2 * a * b, a * b * b + c - u)
        if max(x1, x2) == v:
            ans += 1
print(ans)
