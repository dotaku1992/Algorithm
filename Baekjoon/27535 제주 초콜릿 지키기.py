import sys


def makeFirstans(h, t, c, k, g, prevdigit):
    sumNum = h + t + c + k + g
    if prevdigit == 0 or prevdigit == 1:
        return str(sumNum)
    else:
        output = ''
        while sumNum > 0:
            output = output + str(sumNum % prevdigit)
            sumNum //= prevdigit
        return output[::-1] if output else '0'


H, T, C, K, G = map(int, sys.stdin.readline().rstrip().split())
m = int(sys.stdin.readline().rstrip())
for _ in range(m):
    dh, dt, dc, dk, dg = map(int, sys.stdin.readline().rstrip().split())
    prevNum = H + T + C + K + G
    H, T, C, K, G = H - dh, T - dt, C - dc, K - dk, G - dg
    firstAns = makeFirstans(H, T, C, K, G, prevNum % 10) + '7H'
    print(firstAns)

    arr = [(cnt, alphavet) for cnt, alphavet in zip([H, T, C, K, G],
                                                    ['H', 'T', 'C', 'K', 'G'])]
    arr.sort(key=lambda x: (-x[0], x[1]))
    secondans = ''
    for c, a in arr:
        if c != 0:
            secondans += a

    print(secondans if ((H + T + C + K + G) != 0) else 'NULL')
