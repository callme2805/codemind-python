import math
x,y,m=map(int,input().split())
s=math.pow(x,y)
p=s%m
print(int(p))