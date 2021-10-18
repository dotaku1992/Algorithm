n = int(input())
cur_car_cnt = int(input())
ans = cur_car_cnt

for _ in range(n):
    carin, carout = map(int, input().split())
    cur_car_cnt = cur_car_cnt + carin - carout
    if cur_car_cnt < 0:
        print(0)
        ans = -1
        break
    ans = max(ans, cur_car_cnt)
print(ans if ans != -1 else "")
