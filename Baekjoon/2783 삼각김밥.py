X,Y = map(int,input().split())
N = int(input())
price_list = [X/Y*1000]
for _ in range(N):
    mX,mY = map(int,input().split())
    price_list.append(mX/mY*1000)
print(f"{min(price_list):.2f}")