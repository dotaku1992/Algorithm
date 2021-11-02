from itertools import permutations
def isTimecorrect(time):
    return 1<= int(time[0])<=12 and 0<=int(time[1])<60 and 0<=int(time[2])<60

arr = list(input().split(':'))
permu = list(permutations(arr,3))
ans = 0
for ele in permu:
    if isTimecorrect(ele):
        ans+=1
print(ans)