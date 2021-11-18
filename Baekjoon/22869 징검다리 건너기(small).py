n,k = map(int,input().split())
arr = list(map(int,input().split()))
iscanarrive = [0]*n
iscanarrive[0]=1
for idx,_ in enumerate(iscanarrive):
    if iscanarrive[idx]:
        for nidx in range(idx+1,n):
            power = (nidx-idx)*(1+abs(arr[nidx]-arr[idx]))
            if power <=k:
                iscanarrive[nidx]=1
print("YES" if iscanarrive[-1] else "NO")