start = int(input())
ans = 0
anssec = None
for sec in range(1,start+1):
    n1,n2 = start,sec
    cnt=2
    while(n1-n2 >=0):
        n1,n2=n2,n1-n2
        cnt+=1
        if(ans < cnt):
            ans=cnt
            anssec=sec
print(ans)

def sol(a,b):
    if(b<0):
        print(a)
        return
    print(a,end=' ')
    sol(b,a-b)
sol(start,anssec)