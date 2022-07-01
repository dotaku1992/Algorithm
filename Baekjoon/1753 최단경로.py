import sys
from collections import defaultdict
import heapq

INF = 300000 * 100
vn, en = map(int, input().split())
start = int(input())
linktable = defaultdict(dict)
for _ in range(en):
    u, v, w = map(int, sys.stdin.readline().rstrip().split())
    if v in linktable[u]:
        linktable[u][v] = min(w, linktable[u][v])
    else:
        linktable[u][v] = w

djak = []
dist = defaultdict(lambda: INF)
dist[start] = 0
heapq.heappush(djak, (0, start))
while djak:
    curdist, curvertex = heapq.heappop(djak)
    if curdist < dist[curvertex]:
        continue
    for nxtvertex in linktable[curvertex]:
        if curdist + linktable[curvertex][nxtvertex] < dist[nxtvertex]:
            dist[nxtvertex] = curdist + linktable[curvertex][nxtvertex]
            heapq.heappush(djak, (curdist + linktable[curvertex][nxtvertex], nxtvertex))

for i in range(1, vn + 1):
    print(dist[i] if dist[i] != INF else "INF")
