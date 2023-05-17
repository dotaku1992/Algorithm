import sys

x, N = map(int, sys.stdin.readline().rstrip().split())
for _ in range(N):
    if x % 2 == 0:
        x = (x // 2) ^ 6
    else:
        x = (2 * x) ^ 6
print(x)
