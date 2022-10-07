import sys

n = int(sys.stdin.readline().rstrip())
arr = list(map(int, sys.stdin.readline().rstrip().split()))  # 높이대 여부는 arr[i] != 0
dp = [0 for _ in range(n)]
for i in reversed(range(0, n)):
    if arr[i]:
        dp[i] = 1 + (dp[i + arr[i] + 1] if i + arr[i] + 1 < n else 0)
    else:
        dp[i] = 1 + (dp[i + 1] if i + 1 < n else 0)

print(*dp)
