n = int(input())

if n == 0:
    print(0)
elif n == 1:
    print(1)
else:
    n -= 1
    n2, n1 = 1, 0
    for _ in range(n):
        n2, n1 = n2 + n1, n2
    print(n2)
