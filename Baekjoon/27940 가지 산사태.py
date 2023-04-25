import sys

n, m, maxheight = map(int, sys.stdin.readline().rstrip().split())

# 항상 왼쪽 배열(저층)이 가장 먼저 물이 찬다 -> 잠긴다면 항상 1층은 잠긴다는 의미
cnt = 0
for i, _ in enumerate(range(m), 1):
    _, r = map(int, sys.stdin.readline().rstrip().split())
    if cnt + r > maxheight:
        print(i, 1)
        break
    cnt += r
else:
    print(-1)
