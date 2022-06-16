def solution(array, commands):
    answer = []
    for i, j, k in commands:
        subarr = [array[idx] for idx in range(i - 1, j)]
        subarr.sort()
        answer.append(subarr[k - 1])
    return answer
