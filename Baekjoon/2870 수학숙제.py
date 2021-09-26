import re
n = int(input())
ans_list = []
for _ in range(n):
    input_text = input()
    p = re.compile('\d+')
    ans_list += p.findall(input_text)

ans_list = list(map(int,ans_list))
ans_list.sort()
for ele in ans_list:
    print(ele)