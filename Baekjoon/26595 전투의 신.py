import sys
n = int(sys.stdin.readline().rstrip())
a,pt,b,pd = map(int,sys.stdin.readline().rstrip().split())
maxndealer,maxntanker = n//pd , n//pt
arr =[(dt,dn) for dn in range(maxndealer+1) for dt in range(maxntanker+1) if dt*pt + dn*pd <=n]
ans = max(arr,key=lambda x: a*x[0]+b*x[1])
print(*ans)