import sys

n, m, maxvalue = map(int, sys.stdin.readline().rstrip().split())

if n + m - 1 > maxvalue:
    print("NO")
else:
    print("YES")
    for i in range(1, n + 1):
        print(*list(range(i, i + m)))
