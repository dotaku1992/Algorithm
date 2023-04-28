import sys


def isMatch(str1, str2):
    life = 1
    for c1, c2 in zip(str1, str2):
        if c1 == c2:
            continue
        else:
            life -= 1

    if life == 0:
        return True
    else:
        return False


n = int(sys.stdin.readline().rstrip())
texts = sys.stdin.readline().rstrip()

flag = False
for textlen in range(1, n):
    result = isMatch(texts[:textlen], texts[-textlen:])
    flag |= result

print("YES" if flag else "NO")
