from collections import deque

arr = [list(map(int, input().split())) for _ in range(5)]
y, x = map(int, input().split())
isvisited = [[0 for _ in range(5)] for _ in range(5)]
bfs = deque()
bfs.append((y, x, 0))
isvisited[y][x] = 1
dy = [0, 0, 1, -1]
dx = [1, -1, 0, 0]
flag = True
while bfs and flag:
    popy, popx, pstep = bfs.popleft()
    for py, px in zip(dy, dx):
        ny, nx = popy + py, popx + px
        if 0 <= ny < 5 and 0 <= nx < 5 and not isvisited[ny][nx] and arr[ny][nx] != -1:
            isvisited[ny][nx] = 1
            bfs.append((ny, nx, pstep + 1))
            if arr[ny][nx] == 1:
                print(pstep + 1)
                flag = False
                break
if flag:
    print(-1)

# abs(|y|) + abs(|x|)로 최단거리라 생각했는데 막힌경우 돌아가는 방법처럼 실제로는 최단거리지만 갈 수 없는 경우를 생각을 못했다. 실제로 step를 체크했어야했다.
