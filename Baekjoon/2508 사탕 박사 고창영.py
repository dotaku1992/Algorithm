T = int(input())

dy = [0,0,1,-1]
dx = [1,-1,0,0]
dc = ['<','>','^','v']
for _ in range(T):
    input() #빈줄제거
    r,c = map(int,input().split())
    arr = [input() for _ in range(r)]

    ans = 0
    for y in range(r):
        for x in range(c):
            if arr[y][x]=='o':
                flag = [False,False,False,False]
                for idx,(py,px,pc) in enumerate(zip(dy,dx,dc)):
                    ny = y+py
                    nx = x+px
                    if 0<=nx<c and 0<=ny<r and arr[ny][nx]==pc:
                        flag[idx]=True
                ans += (flag[0]&flag[1]) | (flag[2]&flag[3])
    print(ans)