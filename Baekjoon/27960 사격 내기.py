import sys

sa, sb = map(int, sys.stdin.readline().rstrip().split())

# 한명만 맞춘 표적은 맞춤 , 둘이 맞추거나 못맞춘건 안맞춤 : XOR연산에 해당된다.
print(sa ^ sb)
