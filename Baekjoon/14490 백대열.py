import math

a,b = map(int,input().split(':'))
gcd = math.gcd(a,b)
print(f"{a//gcd}:{b//gcd}")