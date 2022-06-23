def solution(d, budget):
    d.sort()
    answer = 0
    for _, val in enumerate(d):
        if val <= budget:
            budget -= val
            answer += 1

    return answer
