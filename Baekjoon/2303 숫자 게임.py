import sys

n = int(input())

ans = None
maxdigit1 = -1
for p in range(n):
    arr = list(map(int, sys.stdin.readline().rstrip().split()))

    for i, j, k in [(i, j, k) for i in range(0, 5) for j in range(i + 1, 5) for k in range(j + 1, 5)]:
        val = (arr[i] + arr[j] + arr[k]) % 10
        if val >= maxdigit1:
            maxdigit1 = val
            ans = p + 1
print(ans)
