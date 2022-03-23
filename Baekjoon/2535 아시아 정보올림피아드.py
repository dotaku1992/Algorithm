from collections import defaultdict
n = int(input())
participates = []

for _ in range(n):
    cont,no,score = map(int,input().split())
    participates.append((cont,no,score))

participates.sort(reverse= True, key = lambda x : x[2])
rank = 1
cont_cnt = defaultdict(int)
for m_c,m_n,m_s in participates:
    if rank>3:
        break
    if cont_cnt[m_c]>=2:
        continue
    else:
        rank+=1
        cont_cnt[m_c]+=1
        print(m_c,m_n)