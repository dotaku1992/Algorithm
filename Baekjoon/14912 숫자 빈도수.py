n,digit = map(int,input().split())
digit = str(digit)
ans = 0
for i in range(1,n+1):
    ans+=str(i).count(digit)
print(ans)