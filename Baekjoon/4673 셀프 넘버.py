save_data = [0]*10001

def dn(n : int):
    return n+sum(map(int,list(str(n))))

for val in range(1,10001):
    value = dn(val)
    if value<=10000:
        save_data[value]=1
for val in range(1,10001):
    if save_data[val]==0:
        print(val)