def solution(absolutes, signs):
    answer = sum([v*(1 if m else -1) for v,m in zip(absolutes,signs)])
    return answer