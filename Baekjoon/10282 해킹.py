import sys
import heapq
from collections import defaultdict
import math

T = int(sys.stdin.readline().rstrip())

for _ in range(T):
    n, d, start = map(int, sys.stdin.readline().rstrip().split())
    linktable = defaultdict(lambda: defaultdict(int))
    for _ in range(d):
        a, b, s = map(int, sys.stdin.readline().rstrip().split())
        linktable[b][a] = s

    distances = [float('inf') for _ in range(n + 1)]
    queue = []
    distances[start] = 0
    heapq.heappush(queue, [0, start])
    while queue:
        pop_distance, pop_vertex = heapq.heappop(queue)
        if pop_distance < distances[pop_vertex]:
            continue
        for nxtvertex, length in linktable[pop_vertex].items():
            if pop_distance + linktable[pop_vertex][nxtvertex] < distances[nxtvertex]:
                distances[nxtvertex] = pop_distance + linktable[pop_vertex][nxtvertex]
                heapq.heappush(queue, [pop_distance + linktable[pop_vertex][nxtvertex], nxtvertex])
    foranserArr = [dist for dist in distances[1:] if not math.isinf(dist)]
    print(len(foranserArr), max(foranserArr))
