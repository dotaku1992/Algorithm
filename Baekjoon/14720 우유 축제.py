n = int(input())
store = list(map(int,input().split()))

cur = 0
ans = 0
for ele in store:
    if cur == ele:
       ans+=1
       cur = (cur+1)%3
print(ans)