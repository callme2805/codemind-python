N=int(input())
M=list(map(int,input().split()))
a=[]
b=[]
for i in M:
    if i%2:
        a.append(i)
    else:
        b.append(i)
b.extend(a)
print(*b)