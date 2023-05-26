import sys

text = sys.stdin.readline().rstrip()
ans = all([c in text for c in "MOBIS"])
print("YES" if ans else "NO")
