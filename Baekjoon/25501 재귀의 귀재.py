import sys

T = int(sys.stdin.readline().rstrip())

for _ in range(T):
    text = sys.stdin.readline().rstrip()
    isPalindrome = True
    anscnt = 0
    for i in range(len(text) // 2):
        anscnt += 1
        if text[i] != text[-(i + 1)]:
            isPalindrome = False
            break
    else:
        anscnt += 1

    print(int(isPalindrome), anscnt)
