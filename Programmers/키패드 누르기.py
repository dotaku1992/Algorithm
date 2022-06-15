# lv1
def getdist(p, g):
    return abs(g[0] - p[0]) + abs(g[1] - p[1])


def solution(numbers, hand):
    posdict = {1: (0, 0), 2: (0, 1), 3: (0, 2), 4: (1, 0), 5: (1, 1), 6: (1, 2), 7: (2, 0), 8: (2, 1), 9: (2, 2),
               '*': (3, 0), 0: (3, 1), '#': (3, 2)}
    lpos = posdict['*']
    rpos = posdict['#']
    answer = ''
    for ele in numbers:
        if posdict[ele][1] == 0:
            lpos = posdict[ele]
            answer += 'L'
        elif posdict[ele][1] == 2:
            rpos = posdict[ele]
            answer += 'R'
        else:
            if getdist(posdict[ele], lpos) == getdist(posdict[ele], rpos):
                answer += hand[0].upper()
                if answer[-1] == 'L':
                    lpos = posdict[ele]
                else:
                    rpos = posdict[ele]
            else:
                if getdist(posdict[ele], lpos) < getdist(posdict[ele], rpos):
                    answer += 'L'
                    lpos = posdict[ele]
                else:
                    answer += 'R'
                    rpos = posdict[ele]

    return answer
