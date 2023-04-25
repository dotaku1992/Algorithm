import sys
from collections import defaultdict

n = int(sys.stdin.readline().rstrip())
texts = list(sys.stdin.readline().rstrip())
check = defaultdict(str)
flag = True
for textlen in range(1, n + 1):
    for idx, c in enumerate(texts):
        if idx + textlen > n:
            continue
        else:
            for sidx in range(idx, idx + textlen):
                savec = texts[sidx]
                texts[sidx] = '?'
                changedtxt = ''.join(texts[idx:idx + textlen])
                texts[sidx] = savec
                if changedtxt in check and check[changedtxt] != savec:
                    flag = False
                else:
                    check[changedtxt] = savec

print("YES" if not flag else "No")
