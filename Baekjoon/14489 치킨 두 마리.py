b1,b2 = map(int,input().split())
price = int(input())
print(b1+b2-2*price if 2*price <= b1+b2 else b1+b2)