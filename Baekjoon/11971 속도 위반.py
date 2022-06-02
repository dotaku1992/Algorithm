n, m = map(int, input().split())
limits = []
driver = []

for _ in range(n):
    dist, velocity = map(int, input().split())
    limits.extend([velocity for _ in range(dist)])

for _ in range(m):
    dist, velocity = map(int, input().split())
    driver.extend([velocity for _ in range(dist)])

ans = 0

for l, d in zip(limits, driver):
    ans = max(ans, d - l)
print(ans)
