a,b = map(int,input().split())
a = a-1
b = b-1
a_x,a_y = a//4,a%4
b_x,b_y = b//4,b%4
print(abs(b_x-a_x)  + abs(b_y-a_y))