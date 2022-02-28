n,m,l = map(int,input().split())

arr = [0 for i in range(n)]
idx = 0
throw_cnt = 0
arr[0]=1
while(True):
    if arr[idx]==m:
        break
    if arr[idx] & 1:
        idx = (idx + l)%n
    else:
        idx = (n+idx-l)%n
    arr[idx]+=1
    throw_cnt+=1

print(throw_cnt)