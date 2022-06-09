import sys

def getidx(h):
    return h // 2

sh, sm = map(int, input().split(':'))
arr = list(map(int, input().split()))
onoff = [1] * 6
ph, pm = 0, 0
n = int(input())
for _ in range(n):
    sec, cmd = sys.stdin.readline().rstrip().split()
    sec, msec = map(int, sec.split('.'))
    if cmd == '^':
        curm = sm + pm + (sec // 60)
        curh = sh + ph + (curm // 60)
        curm, curh = curm % 60, curh % 12
        onoff[getidx(curh)] = 0
    elif 'HOUR' in cmd:
        ph += int(cmd[0:1])
    else:
        pm += int(cmd[0:2])
ans = min(100, sum([arr[idx] * onoff[idx] for idx in range(6)]))
print(ans)
