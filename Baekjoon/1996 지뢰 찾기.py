n = int(input())
cnt = [[0 for _ in range(n)] for _ in range(n)]
inputs = [input() for _ in range(n)]

dx = [0, 0, 1, -1, 1, -1, 1, -1]
dy = [1, -1, 0, 0, 1, 1, -1, -1]
for y in range(n):
    for x in range(n):
        if inputs[y][x] != '.':
            num = int(inputs[y][x])
            for py, px in zip(dy, dx):
                if 0 <= x + px < n and 0 <= y + py < n:
                    cnt[y + py][x + px] += num

for y in range(n):
    for x in range(n):
        if inputs[y][x] != '.':
            print('*', end='')
        elif cnt[y][x] >= 10:
            print('M', end='')
        else:
            print(cnt[y][x], end='')
    print()
