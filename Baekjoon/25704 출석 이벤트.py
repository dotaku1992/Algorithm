import sys

N = int(sys.stdin.readline().rstrip())
S = int(sys.stdin.readline().rstrip())
P = S
if N >= 5:
    P = min(P, S - 500)
if N >= 10:
    P = min(P, S * 90 // 100)
if N >= 15:
    P = min(P, S - 2000)
if N >= 20:
    P = min(P, S * 75 // 100)
print(max(0, P))
