def An(n):
    if n==1:
        return 1
    else:
        return 6*(n-1)


num = int(input())
ans = 1
while(An(ans) <num):
    num -=An(ans)
    ans+=1
print(ans)
