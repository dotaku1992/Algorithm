import sys

n, game = sys.stdin.readline().rstrip().split()
names = set([sys.stdin.readline().rstrip() for _ in range(int(n))])
dictcntplayers = {'Y': 1, 'F': 2, 'O': 3}
print(len(names) // dictcntplayers[game])
