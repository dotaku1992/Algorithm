import sys
from collections import defaultdict

subject = {'kor': 0, 'eng': 1, 'math': 2}
fruit = {'apple': 0, 'pear': 1, 'orange': 2}
color = {'red': 0, 'blue': 1, 'green': 2}
n, m = map(int, input().split())

cnt = defaultdict(int)

for _ in range(n):
    s, f, c = sys.stdin.readline().rstrip().split()
    cnt[(subject[s], fruit[f], color[c])] += 1

for _ in range(m):
    cmd = [[func[ele]] if ele != '-' else [0, 1, 2] for func, ele in
           zip((subject, fruit, color), sys.stdin.readline().rstrip().split())]
    ans = 0
    anslist = [cnt[(s, f, c)] for s in cmd[0] for f in cmd[1] for c in cmd[2]]
    print(sum(anslist))
