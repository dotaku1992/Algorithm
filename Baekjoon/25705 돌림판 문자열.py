import sys
from collections import deque

n1 = int(sys.stdin.readline().rstrip())
beforeArr = deque(list(sys.stdin.readline().rstrip()))
n2 = int(sys.stdin.readline().rstrip())
afterArr = sys.stdin.readline().rstrip()
idx = 0
maxlen = len(afterArr)
answer = 0
if not set(afterArr).issubset(set(beforeArr)):
    print(-1)
    sys.exit(0)

while idx < maxlen:
    answer += 1
    beforeArr.append(beforeArr.popleft())
    if afterArr[idx] == beforeArr[-1]:
        idx += 1

print(answer)
