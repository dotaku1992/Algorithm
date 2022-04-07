from collections import deque
import sys

v, e = map(int, sys.stdin.readline().rstrip().split())
table = [[0 for _ in range(v + 1)] for _ in range(v + 1)]
is_visited = [0 for _ in range(v + 1)]

for _ in range(e):
    v1, v2 = map(int, sys.stdin.readline().rstrip().split())
    table[v1][v2] = table[v2][v1] = 1
ans = 0

for vertex in range(1, v + 1):
    if not is_visited[vertex]:
        ans += 1
        is_visited[vertex] = 1
        bfs = deque()
        bfs.append(vertex)
        while bfs:
            cur_v = bfs.popleft()
            for nxtvertex in range(1, v + 1):
                if not is_visited[nxtvertex] and table[cur_v][nxtvertex]:
                    bfs.append(nxtvertex)
                    is_visited[nxtvertex] = 1
print(ans)
