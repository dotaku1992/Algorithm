a,b = map(int,input().split())

if a>=0:
    q,r =abs(a)//abs(b),abs(a)%abs(b)
    q = q if b >=0 else -q
    print(q,r,sep="\n")
else:
    if abs(a)%abs(b)==0:
        q=a//b
        r=0
    else:
        q=abs(a)//abs(b)+1
        q = q if b <0 else -q
        r = a-q*b
    print(q, r, sep="\n")
