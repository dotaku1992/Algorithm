N = int(input())
sx, sy, ex, ey = map(int, input().split())
ansarr = []
for no in range(N):
    pointN = int(input())
    dist = 0
    arr = [tuple(map(int, input().split())) for _ in range(pointN)]
    arr = [(sx, sy)] + arr + [(ex, ey)]
    for idx, (x, y) in enumerate(arr[:-1]):
        nxtx, nxty = arr[idx + 1]
        dist += abs(x - nxtx) + abs(y - nxty)
    ansarr.append((no + 1, dist))

print(min(ansarr, key=lambda x: x[1])[0])
