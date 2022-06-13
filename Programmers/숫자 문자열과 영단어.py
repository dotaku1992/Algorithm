#lv1
def solution(s):
    table = {'': '', 'zero': '0', 'one': '1', 'two': '2', 'three': '3', 'four': '4', 'five': '5', 'six': '6',
             'seven': '7', 'eight': '8', 'nine': '9'}
    subtext = ''
    answer = ''
    for ele in s:
        if '0' <= ele <= '9':
            answer += ele
        else:
            subtext += ele
            if subtext in table:
                answer += table[subtext]
                subtext = ''
    answer += table[subtext]
    return int(answer)
