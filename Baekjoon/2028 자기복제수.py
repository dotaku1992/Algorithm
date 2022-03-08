import math
T = int(input())

for _ in range(T):
    num = int(input())
    l = int(math.log10(num))+1
    sqnum = num*num%(10**l)
    print("YES" if num == sqnum else "NO")
