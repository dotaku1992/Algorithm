def solution(numbers):
    answer = []
    maxlen = len(numbers)
    for i in range(maxlen):
        for j in range(i+1,maxlen):
            answer.append(numbers[i]+numbers[j])
    #answer = list(set(sorted(answer))) "set은 순서가 보상되지 않아서 set할 list가 정렬되어있다해도 set을 적용하게 되면 순서가 바뀐다 그러므로 맨마지막에 sorted를 해줘야한다."
    answer = sorted(list(set(answer)))
    return answer