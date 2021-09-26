a,b,c,d = map(int,input().split())
person = list(map(int,input().split()))
# a분동안 공격적이고 b분 휴식
# c분동안 공격적이고 d분 휴식
# P 우체부 도착시간 M 우유 ,
dog1 = [1]*a + [0]*b
dog2 = [1]*c + [0]*d
for p in person:
    print(dog1[(p-1)%(a+b)] + dog2[(p-1)%(c+d)])
