def solution(left, right):
    answer = 0
    for num in range(left, right + 1):
        cnt = 0
        for div in range(1, num + 1):
            if num % div == 0:
                cnt += 1
        if cnt & 1:
            answer -= num
        else:
            answer += num
    return answer
