# lv1
from collections import defaultdict


def solution(participant, completion):
    check = defaultdict(int)
    answer = ''
    for name in participant:
        check[name] += 1
    for name in completion:
        check[name] -= 1
    for name, cnt in check.items():
        if cnt == 1:
            answer = name

    return answer
