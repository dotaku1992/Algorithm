n,r = map(int,input().split())
a,b=[],[]
for _ in range(n):
    a.append(list(map(int,input().split())))
for _ in range(n):
    b.append(list(map(int,input().split())))

ans = [[a[y][x]+b[y][x] for x in range(r)] for y in range(n)]
for y in range(n):
    for x in range(r):
        print(ans[y][x],end=' ')
    print()