#네이버였는지 NHN이였는지 1번문제에서 비슷한 문제가 나왔던 기억이 난다.
#당시에는 문자별로 idx를 기록해서 dfs로 풀었지만 이런 경우에는 부분문자열이 성립할 경우 차례대로 확인하면 되었던 기억이 있다.
from collections import deque
while True:
    try:
        subtext,alltext = input().split()
        deq_sub_text = deque(subtext)

        for c in alltext:
            if deq_sub_text and deq_sub_text[0]==c:
                deq_sub_text.popleft()
        if not deq_sub_text:
            print("Yes")
        else:
            print("No")

    except:
        break