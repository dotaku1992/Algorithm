import sys

n = int(input())
arr = list(map(int, sys.stdin.readline().rstrip().split()))
l, r = arr[0], arr[1]
for ele in arr[2:]:
    if l == r:
        l += ele
    else:
        if l < r:
            l += ele
        else:
            r += ele
diffOfWeight = abs(l - r)
ans = 0
for div in [100, 50, 20, 10, 5, 2, 1]:
    q = diffOfWeight // div
    ans += q
    diffOfWeight -= q * div
print(ans)
