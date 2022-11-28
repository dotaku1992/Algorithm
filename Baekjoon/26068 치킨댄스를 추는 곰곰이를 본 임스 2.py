import sys

n = int(sys.stdin.readline().rstrip())
arr = [int(sys.stdin.readline().rstrip().split('-')[1]) for _ in range(n)]
filtedarr = list(filter(lambda x: x <= 90, arr))
print(len(filtedarr))
