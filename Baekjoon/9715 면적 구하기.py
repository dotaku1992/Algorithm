t = int(input())
dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]
for _ in range(t):
    r, c = map(int, input().split())
    arr = [list(map(int, list(input()))) for _ in range(r)]
    area = [[4 * arr[y][x] + 2 for x in range(c)] for y in range(r)]
    ans = 0
    for y in range(r):
        for x in range(c):
            if arr[y][x]:
                for idx in range(4):
                    py, px = y + dy[idx], x + dx[idx]
                    if 0 <= px < c and 0 <= py < r and arr[py][px]:
                        area[y][x] -= min(arr[y][x], arr[py][px])
                ans += area[y][x]
    print(ans)
