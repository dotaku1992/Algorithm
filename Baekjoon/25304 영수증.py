X = int(input())
n = int(input())
for _ in range(n):
    p, num = map(int, input().split())
    X -= p * num
print("Yes" if X == 0 else "No")
