import sys
badcombination = [[0 for _ in range(201)] for _ in range(201)]

n,m = map(int,input().split())
for _ in range(m):
    i,j = map(int,sys.stdin.readline().rstrip().split())
    badcombination[i][j]=badcombination[j][i]=1
ans = n*(n-1)*(n-2)//6
for i in range(1,n+1):
    for j in range(i+1,n+1):
        for k in range(j+1, n+1):
            if badcombination[i][j]+badcombination[i][k]+badcombination[j][k]>=1:
                ans-=1
print(ans)