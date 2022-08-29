import re
n, k = map(int, input().split())

def makeDigit(tennum: int, digit: int) -> str:
    output = ''
    while (True):
        output += str(tennum % digit)
        tennum //= digit
        if not tennum:
            break
    return output[::-1]

splitedarr = re.split(r'0+',makeDigit(n,k))
splitedarr = list(filter(lambda x : x , splitedarr)) # 빈문자열 제거용도 input이 3 3일경우에 splitedarr에는 ['1',''] 3이 3진수로 바뀐 10 3진수가 있고 0으로 split할경우 맨뒤의 빈문자열이 에러를 일으켰음
sumarr = sum(map(int,splitedarr))

print(makeDigit(sumarr,k))