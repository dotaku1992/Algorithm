from collections import deque

n,m,start = map(int,input().split())

connect = [[0 for _ in range(n+1)] for _ in range(n+1)]

for _ in range(m):
    a,b = map(int,input().split())
    connect[a][b]=connect[b][a]=1

isvisited = [0 for _ in range(n+1)]
dfs = []
dfs.append(start)
while dfs:
    p=dfs.pop()
    if not isvisited[p]:
        print(p, end=' ')
        isvisited[p]=1
    for i in range(n,0,-1):
        if connect[p][i] and not isvisited[i]:
            dfs.append(i)
print()

bfs = deque()
isvisited = [0 for _ in range(n+1)]
bfs.append(start)
isvisited[start]=1
while bfs:
    p = bfs.popleft()
    print(p,end = ' ')
    for i in range(1,n+1):
        if connect[p][i] and not isvisited[i]:
            isvisited[i]=1
            bfs.append(i)
print()
