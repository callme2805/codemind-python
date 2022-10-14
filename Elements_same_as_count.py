n=int(input())
l=list(map(int,input().split()))
a=[]
c=0
for i in range(n):
    if l[i]==l.count(l[i]):
        a.append(l[i])
        c=1
if c==1:
    b=[]
    for i in a:
        if i not in b:
            b.append(i)
    print(*b)
else:
    print("-1")