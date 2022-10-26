n,m=map(int,input().split())
a=list(map(int,input().split()))
b=list(map(int,input().split()))
k=[]
l=[]
for i in a:
    if i not in k:
        k.append(i)
for i in b:
    if i not in l:
        l.append(i)
p=[]
for i in k:
    if i in l:
        p.append(i)
print(*p)