from collections import defaultdict
from collections import deque
n_com = int(input())
linktable = [[0 for _ in range(n_com+1)] for _ in range(n_com+1)]
n = int(input())
for _ in range(n):
    s,e = map(int,input().split())
    linktable[s][e]=1
    linktable[e][s]=1

isinfect = [0 for _ in range(n_com+1)]
bfs = deque()
bfs.appendleft(1)
isinfect[1]=1
ans = 0
while bfs:
    p = bfs.popleft()
    for idx in range(n_com+1):
        if linktable[p][idx]==1 and isinfect[idx]==0:
            bfs.appendleft(idx)
            isinfect[idx]=1
            ans+=1
print(ans)