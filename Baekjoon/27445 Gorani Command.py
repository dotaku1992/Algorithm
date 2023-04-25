import sys

n, m = map(int, sys.stdin.readline().rstrip().split())
dist = []

for _ in range(n - 1):
    dist.append(int(sys.stdin.readline().rstrip()))
if m != 1:
    dist.extend(list(map(int, sys.stdin.readline().rstrip().split())))
else:
    dist.append(int(sys.stdin.readline().rstrip()))

px, py = 1 + min(dist[:n]), n - min(dist[n - 1:])
print(py, px)
