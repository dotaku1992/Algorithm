import sys
N,M = map(int,input().split())
maxnm = max(N,M)
currentarr = list(map(int,sys.stdin.readline().rstrip().split())) + [0 for _ in range(maxnm-N)]
prevarr = list(map(int,sys.stdin.readline().rstrip().split())) + [0 for _ in range(maxnm-M)]

ans = 0
for c,p in zip(currentarr,prevarr):
    ans = max(ans,p-c)
print(ans)