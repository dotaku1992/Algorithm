import sys

T = int(sys.stdin.readline().rstrip())

for _ in range(T):
    n = int(sys.stdin.readline().rstrip())
    texts = [sys.stdin.readline().rstrip() for _ in range(n)]
    answer = 0
    for i in range(n):
        for j in range(i+1,n):
            text1,text2 = texts[i],texts[j]
            combinedtext1 = text1+text2
            combinedtext2 = text2+text1
            if combinedtext1 == combinedtext1[::-1]:
                answer = combinedtext1
            elif combinedtext2 == combinedtext2[::-1]:
                answer = combinedtext2
            else:
                pass
    print(answer)