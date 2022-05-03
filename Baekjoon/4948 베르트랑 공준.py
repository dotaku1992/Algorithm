import sys

maxn = 123456

isPrime = [1 for _ in range(maxn * 2 + 1)]
isPrime[0] = isPrime[1] = 0
for val in range(2, maxn * 2 + 1):
    if isPrime[val]:
        for mul in range(2, maxn * 2 + 1):
            if val * mul > maxn * 2: break
            isPrime[val * mul] = 0

for idx in range(maxn * 2):
    isPrime[idx + 1] += isPrime[idx]

while (True):
    n = int(sys.stdin.readline().rstrip())
    if not n: break
    print(isPrime[2 * n] - isPrime[n])
