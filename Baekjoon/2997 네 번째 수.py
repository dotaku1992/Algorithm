arr = list(map(int,input().split()))

arr.sort()
d = min(arr[1]-arr[0],arr[2]-arr[1])

for m in range(0,4):
    if min(arr)+d*m not in arr:
        print(min(arr)+d*m)