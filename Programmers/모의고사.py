def solution(answers):
    giveupmaths = [[1, 2, 3, 4, 5], [2, 1, 2, 3, 2, 4, 2, 5, 2, 1, 2, 3, 2, 4, 2, 5],
                   [3, 3, 1, 1, 2, 2, 4, 4, 5, 5, 3, 3, 1, 1, 2, 2, 4, 4, 5, 5, ]]
    maxlen = [len(giveupmaths[i]) for i in range(3)]
    cntans = [0, 0, 0]
    for qidx, ans in enumerate(answers):
        for i in range(3):
            cntans[i] += (giveupmaths[i][qidx % maxlen[i]] == ans)
    maxcnt = max(cntans)
    answer = []
    for i in range(3):
        if maxcnt == cntans[i]:
            answer.append(i + 1)

    return answer
