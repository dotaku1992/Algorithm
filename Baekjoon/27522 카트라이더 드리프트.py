import sys

arr = []

for _ in range(8):
    record, team = sys.stdin.readline().rstrip().split()
    arr.append((record, team))

arr.sort(key=lambda x: x[0])

blue, red = 0, 0
scores = [10, 8, 6, 5, 4, 3, 2, 1]

for idx, (_, t) in enumerate(arr):
    if t == 'B':
        blue += scores[idx]
    else:
        red += scores[idx]

print("Red" if red > blue else "Blue")
