from collections import deque

n, m = map(int, input().split())

arr = [input() for _ in range(n)]
is_visit = [[0 for _ in range(m)] for _ in range(n)]
DY = [1, -1, 0, 0]
DX = [0, 0, 1, -1]
ans = 0

for y in range(n):
    for x in range(m):
        if not is_visit[y][x]:
            ans += 1
            is_visit[y][x] = 1
            bfs = deque()
            bfs.append((y, x))
            idxrange = (0, 2) if arr[y][x] == '|' else (2, 4)
            while bfs:
                py, px = bfs.popleft()
                for dy, dx in zip(DY[idxrange[0]:idxrange[1]], DX[idxrange[0]:idxrange[1]]):
                    ny = py + dy
                    nx = px + dx
                    if 0<=nx <m and 0<=ny<n and not is_visit[ny][nx] and arr[ny][nx]==arr[py][px]:
                        is_visit[ny][nx]=1
                        bfs.append((ny,nx))
print(ans)