import sys
from collections import deque

dx = [1, -1, 0, 0, 0, 0]
dy = [0, 0, 1, -1, 0, 0]
dz = [0, 0, 0, 0, 1, -1]

m, n, h = map(int, sys.stdin.readline().rstrip().split())
arr = [[list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(n)] for _ in range(h)]

areacnt = m * n * h
totcnt = 0
emptyareacnt = 0
bfs = deque()
for z in range(h):
    for y in range(n):
        for x in range(m):
            if arr[z][y][x] == 1:
                totcnt += 1
                bfs.append((z, y, x, 0))
            elif arr[z][y][x] == -1:
                emptyareacnt += 1
            else:
                pass

ansday = 0
if totcnt + emptyareacnt == areacnt:
    print(0)
else:
    while bfs:
        pz, py, px, day = bfs.popleft()
        for az, ay, ax in zip(dz, dy, dx):
            nz, ny, nx = pz + az, py + ay, px + ax
            if 0 <= nz < h and 0 <= ny < n and 0 <= nx < m and arr[nz][ny][nx] == 0:
                totcnt += 1
                arr[nz][ny][nx] = 1
                bfs.append((nz, ny, nx, day + 1))
                ansday = max(day + 1, ansday)
    print(ansday if totcnt + emptyareacnt == areacnt else -1)
