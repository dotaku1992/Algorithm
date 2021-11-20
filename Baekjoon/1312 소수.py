a,b,n = map(int,input().split())
flag = 0
while True:
    q = a//b
    a -= q*b
    a*=10
    if flag == n:
        print(q)
        break
    flag+=1