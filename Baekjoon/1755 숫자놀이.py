numtotext = {0: 'zero', 1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five', 6: 'six', 7: 'seven', 8: 'eight',
             9: 'nine'}
a, b = map(int, input().split())
arr = []

for num in range(a, b + 1):
    subarr = []
    for c in str(num):
        subarr.append(numtotext[int(c)])
    arr.append((' '.join(subarr), num))

arr.sort(key=lambda x: x[0])
for no, (_, num) in enumerate(arr):
    if no % 10 == 0 and no:
        print()
    print(num, end=' ')
