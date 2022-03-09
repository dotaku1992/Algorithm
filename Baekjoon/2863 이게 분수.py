def rot(arr):
    idxdict = {1:0,3:1,0:2,2:3}
    output = [0]*4
    for nidx,idx in idxdict.items():
        output[nidx]=arr[idx]
    return output

def getValue(arr):
    return arr[0]/arr[2] + arr[1]/arr[3]

arr = []
for _ in range(2):
    arr+= map(int,input().split())

ans = getValue(arr),0
for cnt in range(1,4):
    arr = rot(arr)
    if(getValue(arr) > ans[0]):
        ans = getValue(arr),cnt
print(ans[1])