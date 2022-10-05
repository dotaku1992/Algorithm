import sys

n = int(sys.stdin.readline().rstrip())
arr = list(map(int, sys.stdin.readline().rstrip().split()))
ans = 0
curmin = arr[0]
for ele in arr:
    ans = max(ele - curmin, ans)
    curmin = min(curmin, ele)
print(ans)
