def makekdigit(n:int, k:int):
    output = ""
    while(True):
        output+=str(n%k)
        n//=k
        if not n:
            break

    return output[::-1]


def solution(n, k):

    answer = 0
    for data in list(makekdigit(n,k).split('0')):
        if data: #빈문자열 거름용도
            primeflag = True
            val = int(data)
            if val==1: continue
            for dival in range(2,int(val**0.5)+1):
                if val%dival==0:
                    primeflag=False
                    break

            if primeflag:
                answer+=1


    return answer