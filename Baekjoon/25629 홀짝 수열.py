import sys

oddArr = []
evenArr = []
n = sys.stdin.readline().rstrip()
for num in map(int, sys.stdin.readline().rstrip().split()):
    if num % 2 == 0:
        evenArr.append(num)
    else:
        oddArr.append(num)

print(1 if oddArr and 0 <= (len(oddArr) - len(evenArr)) <= 1 else 0)
