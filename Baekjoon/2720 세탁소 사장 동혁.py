t = int(input())

for _ in range(t):
    coins_cnt = [0]*4
    coins_value = [25,10,5,1]
    cent = int(input())
    for idx in range(4):
        coins_cnt[idx]=cent//coins_value[idx]
        cent = cent-coins_value[idx]*coins_cnt[idx]

    print(coins_cnt[0],coins_cnt[1],coins_cnt[2],coins_cnt[3])

# 25 10 5 1
