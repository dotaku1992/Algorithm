table = {"AA":"A","AG":"C","AC":"A","AT":"G"
         ,"GA":"C","GG":"G","GC":"T","GT":"A"
         ,"CA":"A","CG":"T","CC":"C","CT":"G"
         ,"TA":"G","TG":"A","TC":"G","TT":"T"}

n = int(input())
arr = input()
ans = arr[-1]
arr = arr[:-1][::-1]
for ele in arr:
    ans = table[ele+ans]

print(ans)
