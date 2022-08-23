import math

n, m, a, K = map(int, input().split())
dropedN = n * m - a - (m - K)
maxdropedTeam = math.ceil(dropedN // m)
mindropedTeam = divmod(dropedN, n - 1)
print(n - 1 - (m - 1 == mindropedTeam[0]) * mindropedTeam[1] + 1, n - maxdropedTeam)
