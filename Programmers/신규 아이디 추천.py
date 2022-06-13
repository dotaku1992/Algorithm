#lv1
def solution(new_id):
    text1 = new_id.lower()
    text2 = ''
    for ele in text1:
        if ele.islower() or ('0' <= ele <= '9') or ele in ('_', '-', '.'):
            text2 += ele
    endcnt = 0
    text3 = ''
    for ele in text2:
        if ele == '.':
            endcnt += 1
            if endcnt > 1:
                continue
            text3 += (ele)
        else:
            endcnt = 0
            text3 += (ele)

    if text3 and text3[0] == '.':
        text3 = text3[1:]
    if text3 and text3[-1] == '.':
        text3 = text3[:-1]

    if not text3:
        text3 += 'a'

    text3 = text3[:15]
    if text3[-1] == '.':
        text3 = text3[:-1]
    if len(text3) <= 2:
        while not (len(text3) == 3):
            text3 += (text3[-1])
    answer = text3

    return answer
