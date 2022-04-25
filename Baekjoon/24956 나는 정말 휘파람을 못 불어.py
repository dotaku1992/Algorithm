import sys

n = int(sys.stdin.readline().rstrip())
text = sys.stdin.readline().rstrip()

cnt_w = [0 for _ in range(n)]
idx_h = []
cnt_e = [0 for _ in range(n)]

for idx, c in enumerate(text):
    if c == 'W':
        cnt_w[idx] = 1
    elif c == 'H':
        idx_h.append(idx)
    elif c == 'E':
        cnt_e[idx] = 1
    else:
        pass

for idx in range(1, n):
    cnt_w[idx] += cnt_w[idx - 1]

max_e_cnt = 0
for idx in range(1, n):
    cnt_e[-idx - 1] += cnt_e[-idx]
    max_e_cnt = max(max_e_cnt, cnt_e[-idx - 1])

pow_2 = [None for _ in range(max_e_cnt + 1)]
pow_2[0] = 1


def custompow(n):
    if pow_2[n] is not None:
        return pow_2[n]
    else:
        if n % 2 == 0:
            pow_2[n] = custompow(n // 2) * custompow(n // 2)
        else:
            pow_2[n] = custompow(n // 2) * custompow(n // 2) * 2
        return pow_2[n]


ans = 0
for hidx in idx_h:
    if cnt_e[hidx] > 1:
        ans += cnt_w[hidx] * (custompow(cnt_e[hidx]) - 1 - cnt_e[hidx])
        ans %= 1000000007
print(ans)
