import sys

n = int(sys.stdin.readline().rstrip())

arr = []
for _ in range(n):
    a, b = map(int, sys.stdin.readline().rstrip().split())
    arr.append((a, b))
arr.sort(key=lambda x: x[0])
ans = 0
for x, (a, b) in enumerate(arr, 1):
    ans += a * x + b
print(ans)
