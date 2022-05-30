dp = [0] * 11
dp[1] = 0
dp[2] = 1
for num in range(3, 10 + 1):
    dp[num] = (num // 2) * (num - num // 2) + dp[num // 2] + dp[num - num // 2]
print(dp[int(input())])
