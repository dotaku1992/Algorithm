import sys

d1, d2, x = map(int, sys.stdin.readline().rstrip().split())
# 질량/부피 = 밀도
# d 밀도(g/cm3) x 밀도가 더 높은쪽의 질량비율
dmin, dmax = min(d1, d2), max(d1, d2)
gmin, gmax = 1, x / (100 - x)
ans = (gmin + gmax) / ((gmin / dmin) + (gmax / dmax))
print(f'{ans:0.6f}')