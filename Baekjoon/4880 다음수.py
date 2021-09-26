while True:
    a,b,c = map(int,input().split())
    if a==b==c==0:
        break
    if 2*b == a+c: #등차인경우
        print('AP',c+b-a)
    elif b*b ==a*c:
        print('GP',c*b//a)