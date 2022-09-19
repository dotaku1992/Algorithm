import math

S = int(input())
n = (-1 + math.sqrt(1 + 4 * 2 * S)) / 2
if int(n) % 2 == 0:
    def Sn(n):
        return n * (n + 1) // 2


    print(Sn(int(n) + 1) - S)
else:
    print(0)
