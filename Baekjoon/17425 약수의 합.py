import sys
t=int(input())
table_data = [1]*1000001
def set_table():
    for val in range(2,1000001):
        for mul in range(1,1000001):
            if val*mul > 1000000:
                break
            table_data[val*mul]+=val
    for idx in range(2,1000001):
        table_data[idx] = table_data[idx] + table_data[idx-1]

set_table()

for _ in range(t):
    n = int(sys.stdin.readline().rstrip())
    print(table_data[n])


