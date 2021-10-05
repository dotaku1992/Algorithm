from collections import defaultdict
n = int(input())
students = []
for _ in range(n):
    students.append(input()[::-1])

for idx in range(1,len(students[0])+1):
    cnt = defaultdict(int)
    for stu in students:
        cnt[stu[0:idx]]+=1
    if len(cnt.keys()) == n:
        print(idx)
        break
