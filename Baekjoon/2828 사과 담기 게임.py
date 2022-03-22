n,m = map(int,input().split())
cur_pos = (1,1+m-1)
move_cnt= 0
j = int(input())
for _ in range(j):
    idx = int(input())
    if cur_pos[0]<= idx<=cur_pos[1]:
        continue
    else:
        move1,move2 = abs(idx-cur_pos[0]),abs(idx-cur_pos[1])
        move_cnt +=min(move1,move2)
        if move1 < move2:
            cur_pos = (idx,idx+m-1)
        else:
            cur_pos = (idx-(m-1),idx)
print(move_cnt)

