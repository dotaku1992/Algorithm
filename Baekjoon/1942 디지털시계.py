arr = [0]*24*60*60
def init():
    for i in range(24*60*60):
        idx = i
        h = i//(60*60)
        i-= h*60*60
        h *=1_00_00
        m = (i//(60))
        i -= m*60
        m *=1_00
        s = i
        val = h+m+s
        arr[idx] = int(val%3==0) # 0은 모든 정수의 배수이므로 3의 배수에도 포함이다.

def timetosec(text: str):
    h,m,s = map(int,text.split(":"))
    return h*60*60 + m*60 + s



init()
for _ in range(3):

    first,end = input().split()
    val_first,val_end = timetosec(first),timetosec(end)
    if val_first < val_end:
        print(sum(arr[val_first:val_end+1]))
    else:
        print(sum(arr)-sum(arr[val_end+1:val_first]))