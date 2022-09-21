import sys
from collections import deque

dr = [-1, -1, 1, 1]
dc = [-1, 1, -1, 1]

N = int(sys.stdin.readline().rstrip())
arr = [list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(N)]
bfs = deque()
enemys = []
for y in range(N):
    for x in range(N):
        if arr[y][x] == 2:
            bfs.append((y, x))
        elif arr[y][x] == 1:
            enemys.append((y, x))
        else:
            pass
isvisited = [[0 for _ in range(N)] for _ in range(N)]
candestroyerarr = [[0 for _ in range(N)] for _ in range(N)]

while bfs:
    popy, popx = bfs.popleft()
    for idx in range(4):
        ny, nx = popy + dr[idx], popx + dc[idx]
        if 0 <= ny < N and 0 <= nx < N and not isvisited[ny][nx] & (1 << idx):
            isvisited[ny][nx] |= (1 << idx)
            candestroyerarr[popy + dr[idx]][popx] = 1
            candestroyerarr[popy][popx + dc[idx]] = 1
            bfs.append((ny, nx))

print('Lena' if all([candestroyerarr[y][x] for y, x in enemys]) else 'Kiriya')
