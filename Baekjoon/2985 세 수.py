a,b,c = input().split()

operator = ['+','-','*','/']

for op in operator:
    if eval(a+op+b) == int(c):
        print(a+op+b+'='+c)
    elif int(a) == eval(b+op+c):
        print(a+'='+b+op+c)