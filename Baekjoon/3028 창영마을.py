a,b,c = 1,0,0
cmd = input()

for ch in cmd:
    if ch=='A':
        a,b=b,a
    elif ch == 'B':
        b,c=c,b
    else:
        a,c=c,a
print(a*1+2*b+3*c)
