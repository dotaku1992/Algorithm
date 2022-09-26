import sys
from collections import Counter

N = int(sys.stdin.readline().rstrip())
arr = list(map(int, sys.stdin.readline().rstrip().split()))
print(max(Counter(arr).values()))
