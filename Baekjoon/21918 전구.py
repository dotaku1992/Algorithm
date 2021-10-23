def cmd(arr, a, l, r):
    if a == 1:
        arr[l - 1] = r
    elif a == 2:
        for idx in range(l - 1, r):
            arr[idx] = int(not arr[idx])
    elif a == 3:
        for idx in range(l-1,r):
            arr[idx]=0
    elif a ==4:
        for idx in range(l-1,r):
            arr[idx]=1
    return arr

n, m = map(int, input().split())
light = list(map(int, input().split()))

for _ in range(m):
    a, b, c = map(int, input().split())
    light = cmd(light,a,b,c)
print(' '.join(map(str,light)))