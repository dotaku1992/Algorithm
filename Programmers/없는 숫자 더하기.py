# lv1
def solution(numbers):
    answer = 9*(1+9)//2
    for num in numbers:
        answer-=num
    return answer