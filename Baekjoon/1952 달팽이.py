from collections import deque
dy = [0, 1, 0, -1]
dx = [1, 0, -1, 0]
n, m = map(int, input().split())
vis = [[0 for x in range(m)] for y in range(n)]
curv_cnt = 0
flag = 1
vis[0][0] = 1
moveidx = 0
bfs = deque()
bfs.append((0,0))
while(bfs and flag !=n*m):
    p = bfs.popleft()
    py,px = p[0]+dy[moveidx],p[1]+dx[moveidx]
    if 0<=py <n and 0<=px <m and vis[py][px]==0:
        bfs.append((py,px))
        flag+=1
        vis[py][px]=1
    else:
        curv_cnt+=1
        moveidx+=1
        moveidx%=4
        bfs.append(p)
print(curv_cnt)