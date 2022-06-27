def solution(x):
    answer = True if x % sum([int(ele) for ele in str(x)]) == 0 else False
    return answer
