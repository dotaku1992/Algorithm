from collections import defaultdict
t = int(input())

def func(n : int):
    return n*(n+1)//2

ismake = defaultdict(int)
for a in range(1, 46):
    for b in range(1, 46):
        for c in range(1, 46):
            ismake[func(a) + func(b) + func(c)] = 1

for _ in range(t):
    k = int(input())
    print(ismake[k])