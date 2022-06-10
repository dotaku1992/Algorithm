#lv1
def getRank(n: int):
    if n == 6:
        return 1
    elif n == 5:
        return 2
    elif n == 4:
        return 3
    elif n == 3:
        return 4
    elif n == 2:
        return 5
    else:
        return 6


def solution(lottos, win_nums):
    check = [0 for i in range(46)]
    for ele in win_nums:
        check[ele] = 1
    randomcnt = 0
    correctcnt = 0
    for minele in lottos:
        if minele == 0:
            randomcnt += 1
        else:
            if check[minele] == 1:
                correctcnt += 1
    answer = [getRank(correctcnt + randomcnt), getRank(correctcnt)]
    return answer
