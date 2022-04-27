T =int(input())

is_Prime = [1 for _ in range(1000001)]
is_Prime[1]=0
primelist = []
for val in range(2,1000000):
    if is_Prime[val]:
        primelist.append(val)
        for mul in range(2,1000000):
            if val*mul >100000:
                break
            is_Prime[val*mul]=0

for _ in range(T):
    num = int(input())
    flag = True
    for div in primelist:
        if num%div==0:
            flag=False
    print("YES" if flag else "NO")