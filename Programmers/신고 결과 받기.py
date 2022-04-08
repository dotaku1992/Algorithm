from collections import defaultdict
def solution(id_list, report:str, k):
    idtoidx = defaultdict()

    for idx,id in enumerate(id_list):
        idtoidx[id] = idx

    y_reporter_x_subject = [[0 for _ in id_list] for _ in id_list]

    for text in report:
        re,su = text.split()
        y_reporter_x_subject[idtoidx[re]][idtoidx[su]]=1

    reportcnt = [0 for _ in id_list]

    for x,_ in enumerate(id_list):
        for y,_ in enumerate(id_list):
            reportcnt[x]+=y_reporter_x_subject[y][x]

    answer = [0 for _ in id_list]
    for x, _ in enumerate(id_list):
        for idx, val in enumerate(reportcnt):
            answer[x] += y_reporter_x_subject[x][idx]*(val>=k)


    return answer