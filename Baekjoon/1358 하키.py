w,h,x,y,n = map(int,input().split())

def isincircle(cx,cy,x,y,r):
    if ((x-cx)**2+(y-cy)**2) <=r*r:
        return True
    else:
        return False

ans = 0
for _ in range(n):
    inx,iny = map(int,input().split())
    ans += (x<=inx<=x+w and y<=iny<=y+h) or isincircle(x,y+h//2,inx,iny,h//2) or isincircle(x+w,y+h//2,inx,iny,h//2)
print(ans)