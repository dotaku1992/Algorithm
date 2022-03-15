#pypy3로 제출시 통과 python3 시간초과
import sys
n = int(input())
arr = list(map(int,sys.stdin.readline().rstrip().split()))
ans = 0
for i in range(n):
    for j in range(n):
        ans += abs(arr[i]-arr[j])
print(ans)