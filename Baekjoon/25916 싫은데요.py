import sys
N,M = map(int,sys.stdin.readline().rstrip().split())
arr = list(map(int,sys.stdin.readline().rstrip().split()))
l,r = 0,0
sumval = 0
ans = 0
while l < N or r <N:
    if r <N and sumval+arr[r] <=M:
        sumval+=arr[r]
        r+=1
        ans = max(ans,sumval)
    else:
        sumval-=arr[l]
        l+=1
print(ans)