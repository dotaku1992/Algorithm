from collections import deque

n, k = map(int, input().split())
A = deque(map(int, input().split()))
robots = deque([0 for _ in range(n)])
ans = 0
while k > 0:
    # 1step
    p = A.pop()
    A.appendleft(p)
    robots.pop()
    robots.appendleft(0)
    if robots[-1] == 1:
        robots[-1] = 0

    # 2step
    for i in range(n - 1, -1, -1):
        if robots[i] and not robots[i + 1] and A[i + 1] > 0:
            robots[i + 1] = 1
            robots[i] = 0
            A[i + 1] -= 1
            if not A[i + 1]:
                k -= 1
            if robots[-1] == 1:
                robots[-1] = 0

    # 3step
    if robots[0] == 0 and A[0]:
        robots[0] = 1
        A[0] -= 1
        if not A[0]:
            k -= 1
    ans += 1
print(ans)
