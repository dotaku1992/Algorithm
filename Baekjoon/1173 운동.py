def cantgetexercise(N,m,M,T,R):
    if m + T > M:
        return True
    return False

N,m,M,T,R = map(int,input().split())
et = 0
t = 0
cur_m = m
if cantgetexercise(N,m,M,T,R):
    print(-1)
else:
    while(et != N):
        if cur_m+T <=M:
            cur_m = cur_m+T
            et+=1
        else:
            cur_m = max(m,cur_m-R)
        t+=1
    print(t)