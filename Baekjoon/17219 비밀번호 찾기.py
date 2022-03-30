import sys
from collections import defaultdict

n, m = map(int, sys.stdin.readline().rstrip().split())
adressAndPassword = defaultdict(str)
for _ in range(n):
    ads, password = sys.stdin.readline().rstrip().split()
    adressAndPassword[ads] = password

for _ in range(m):
    ads = sys.stdin.readline().rstrip()
    print(adressAndPassword[ads])
