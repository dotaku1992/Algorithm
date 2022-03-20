n = int(input())
text = ""
for _ in range(2*n-1):
    inp = input()
    if inp =='/':
        inp='//'
    text+=inp
print(eval(text))