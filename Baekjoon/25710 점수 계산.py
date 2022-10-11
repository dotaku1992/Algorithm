# TODO : 나중에 다시 풀어보기
import sys

n = int(sys.stdin.readline().rstrip())
arr = list(set(map(int, sys.stdin.readline().rstrip().split())))
ans = 0
for i in range(len(arr)):
    for j in range(i + 1, len(arr)):
        ans = max(ans, sum(map(int, str(arr[i] * arr[j]))))
print(ans)
