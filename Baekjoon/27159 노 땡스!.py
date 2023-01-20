import sys

n = int(sys.stdin.readline().rstrip())
arr = list(map(int, sys.stdin.readline().rstrip().split()))
arr.sort()
ans = 0
minval = None
for val in arr:
    if minval is None or minval + 1 != val:
        ans += val
    minval = val
print(ans)
