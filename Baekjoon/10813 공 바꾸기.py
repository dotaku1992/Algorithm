n,m = map(int,input().split())
arr = [i for i in range(1,n+1)]

for _ in range(m):
    idx1,idx2 = map(int,input().split())
    arr[idx1-1],arr[idx2-1] = arr[idx2-1],arr[idx1-1]

print(' '.join(map(str,arr)))