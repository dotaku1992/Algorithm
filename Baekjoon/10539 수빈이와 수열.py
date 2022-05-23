n = int(input())
b = list(map(int, input().split()))
a = [b[0] if i == 1 else i * b[i - 1] - (i - 1) * b[i - 2] for i in range(1, n + 1)]
print(*a)
