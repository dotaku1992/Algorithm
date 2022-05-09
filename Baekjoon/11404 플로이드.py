import sys

INF = 10 * 100000000
n = int(sys.stdin.readline().rstrip())
m = int(sys.stdin.readline().rstrip())

dist = [[INF if i != j else 0 for i in range(n + 1)] for j in range(n + 1)]

for _ in range(m):
    a, b, d = map(int, sys.stdin.readline().rstrip().split())
    dist[a][b] = min(dist[a][b], d)

for mid in range(1, n + 1):
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if dist[i][mid] + dist[mid][j] < dist[i][j]:
                dist[i][j] = dist[i][mid] + dist[mid][j]

for i in range(1, n + 1):
    for j in range(1, n + 1):
        print(0 if dist[i][j] == INF else dist[i][j], end=' ')
    print()
