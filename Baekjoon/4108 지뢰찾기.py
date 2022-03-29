dx = [0,0,1,-1,1,-1,1,-1]
dy = [1,-1,0,0,1,-1,-1,1]

while(True):
    y,x = map(int,input().split())
    if (y,x) == (0,0):
        break;

    mine = [[0 for _ in range(x)] for _ in range(y)]
    map_list = []
    for _ in range(y):
        map_list.append(input())

    for yy in range(y):
        for xx in range(x):
            if map_list[yy][xx]=='*':
                for py,px in zip(dy,dx):
                    ny = yy+py
                    nx = xx+px
                    if 0<=nx <x and 0<=ny < y:
                        mine[ny][nx]+=1
    for yy in range(y):
        for xx in range(x):
            print('*' if map_list[yy][xx]=='*' else mine[yy][xx],end='')
        print()