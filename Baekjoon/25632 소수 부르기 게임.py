import sys

A, B = map(int, sys.stdin.readline().rstrip().split())
C, D = map(int, sys.stdin.readline().rstrip().split())
isPrime = [1 for _ in range(1000 + 1)]

for val in range(2, int(1000 ** 0.5) + 1):
    if isPrime[val]:
        for mul in range(2, 1000 // val + 1):
            isPrime[val * mul] = 0
dudxo = [num for num in range(A, B + 1) if isPrime[num]]
dbwls = [num for num in range(C, D + 1) if isPrime[num]]

yjandyt = len(set(dudxo) & set(dbwls))

ytN = len(dudxo) - yjandyt + yjandyt // 2 + yjandyt % 2
yjN = len(dbwls) - yjandyt + yjandyt - (yjandyt // 2 + yjandyt % 2)

print('yt' if ytN > yjN else 'yj')
