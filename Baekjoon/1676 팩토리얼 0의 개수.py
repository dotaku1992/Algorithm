import math

n = int(input())
factor = math.factorial(n)
ans = 0
while(True):
    if factor%10!=0:
        break
    ans+=1
    factor//=10
print(ans)