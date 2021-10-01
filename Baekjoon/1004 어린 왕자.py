tc = int(input())

def is_incircle(cx,cy,r,x,y):
    # 원의 방정식 (x-cx)**2 + (y-cy)**2 <=r*r
    if (x-cx)**2 + (y-cy)**2 <=r*r: return True
    else: return False




for _ in range(tc):
    x1,y1,x2,y2 = map(int,input().split())
    n = int(input())
    ans = 0
    for _ in range(n):
        cx,cy,r = map(int,input().split())
        if is_incircle(cx,cy,r,x1,y1) ^ is_incircle(cx,cy,r,x2,y2):
            ans+=1
    print(ans)