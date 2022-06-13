# lv1
def solution(n):
    answer = 0
    for div in range(1, n + 1):
        if n % div == 0:
            answer += div
    return answer
