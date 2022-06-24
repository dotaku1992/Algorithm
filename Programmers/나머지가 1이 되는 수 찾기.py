def solution(n):
    isPrime = [0,0,1,1] + [1]*(1000001-4)
    for num in range(int(1000000*0.5)):
        if isPrime[num]:
            for mul in range(2,1000000//num+1):
                isPrime[num*mul]=0

    sosu = [num for num,isp in enumerate(isPrime) if isp]

    answer = 0
    for div in sosu:
        if n%div==1:
            answer = div
            break

    return answer