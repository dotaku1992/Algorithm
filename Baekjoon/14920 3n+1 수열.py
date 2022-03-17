def func(n):
    if n%2==0:
        return n//2
    else:
        return 3*n+1
n = int(input())
step = 1
while(True):
    if n == 1:
        break
    else:
        step+=1
        n = func(n)

print(step)