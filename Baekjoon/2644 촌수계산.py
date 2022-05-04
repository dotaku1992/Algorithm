import sys
from collections import defaultdict, deque

n = int(sys.stdin.readline().rstrip())
s, e = map(int, sys.stdin.readline().rstrip().split())

step = int(sys.stdin.readline().rstrip())
isconnect = defaultdict(list)
for _ in range(step):
    a, b = map(int, sys.stdin.readline().rstrip().split())
    isconnect[a].append(b)
    isconnect[b].append(a)

bfs = deque()
is_visited = defaultdict(int)
is_visited[s] = 1
bfs.append((s, 1))
while bfs:
    id, dist = bfs.popleft()
    for nid in isconnect[id]:
        if not is_visited[nid]:
            bfs.append((nid, dist + 1))
            is_visited[nid] = dist + 1

print(-1 if not is_visited[e] else is_visited[e] - 1)
