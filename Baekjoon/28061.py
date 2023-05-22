import sys

n = int(sys.stdin.readline().rstrip())
arr = list(map(int, sys.stdin.readline().rstrip().split()))
ans = 0
for idx, val in enumerate(arr):
    ans = max(ans, val - n + idx)

print(ans)
