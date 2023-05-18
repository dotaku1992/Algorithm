import sys

n, m, a, b = map(int, sys.stdin.readline().rstrip().split())
ismatch = [0 for _ in range(n + 1)]
isreach = [(0, 1e9) for _ in range(n + 1)]

for _ in range(m):
    l, r = map(int, sys.stdin.readline().rstrip().split())
    for i in range(l, r + 1):
        ismatch[i] = 1
isreach[0] = (1, 0)  # 도달여부,cnt

for idx in range(n + 1):
    if ismatch[idx]:
        continue
    if isreach[idx][0]:
        adist, bdist = idx + a, idx + b
        if adist <= n and not ismatch[adist]:
            isreach[adist] = (1, min(isreach[adist][1], isreach[idx][1] + 1))
        if bdist <= n and not ismatch[bdist]:
            isreach[bdist] = (1, min(isreach[bdist][1], isreach[idx][1] + 1))
print(isreach[n][1] if isreach[n][0] else -1)
