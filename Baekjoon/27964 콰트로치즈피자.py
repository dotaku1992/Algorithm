import sys
import re
from collections import defaultdict

n = int(sys.stdin.readline().rstrip())
topping = list(sys.stdin.readline().rstrip().split())
cheesename = defaultdict(int)
patten = re.compile(r'Cheese$')
for name in topping:
    flag = patten.search(name)
    if flag:
        cheesename[name] = 1
print("yummy" if len(cheesename.keys()) >= 4 else "sad")
