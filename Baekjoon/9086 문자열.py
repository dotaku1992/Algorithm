import sys

T = int(input())
for _ in range(T):
    text = sys.stdin.readline().rstrip()
    print(text[0], text[-1], sep="")
