A, B = map(int, input().split())
n = int(input())
favoritlist = []
for _ in range(n):
    favoritlist.append(int(input()))
favoritmin_distance = min(favoritlist, key=lambda x: abs(x - B))

if abs(A - B) <= abs(favoritmin_distance - B):
    print(abs(B - A))
else:
    print(1 + abs(B - favoritmin_distance))
