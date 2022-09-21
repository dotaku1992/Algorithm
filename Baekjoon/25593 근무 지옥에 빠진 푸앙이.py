import sys
from collections import defaultdict

N = int(sys.stdin.readline().rstrip())
workTimeOfName = defaultdict(int)
Times = [4, 6, 4, 10]
for _ in range(N):
    for i in range(4):
        input_texts = list(sys.stdin.readline().rstrip().split())
        for input_text in input_texts:
            if input_text != '-':
                workTimeOfName[input_text] += Times[i]

valueArr = workTimeOfName.values()
print('Yes' if (not valueArr or max(valueArr) - min(valueArr) <= 12) else 'No')
