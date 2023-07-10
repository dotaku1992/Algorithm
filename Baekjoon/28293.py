import sys
import math

a, b = map(int, sys.stdin.readline().rstrip().split())

print(int(b * math.log10(a)) + 1)
