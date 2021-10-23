def cmdfunction(cur_w,cmd,n):
    if cmd == 'E': return cur_w-n
    else : return cur_w +n

sina = 1
while True:
    ideal_w,real_w = map(int,input().split())
    if (ideal_w,real_w) == (0,0):
        break
    #E : exercise , F : feed
    # 운동은 입력된 숫자(n)만큼 지나면 체중n감소
    # 먹이를 먹으면 뚱둥 입력된숫자(n)만큼 체중 증가
    isDie = False
    while True:
        cmd,n = input().split()
        if cmd == '#':
            break
        if not isDie:
            real_w = cmdfunction(real_w,cmd,int(n))
            if real_w <=0: isDie=True


    feeling = "RIP" if isDie else ":-)" if real_w >ideal_w/2 and real_w <ideal_w*2 else ":-("
    print(f"{sina} {feeling}")
    sina +=1
