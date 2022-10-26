n,m=map(int,input().split())
a=list(map(int,input().split()))
b=list(map(int,input().split()))
l=list(set(a))
k=list(set(b))
c=[]
for i in l:
    if i not in k:
        c.append(i)
for i in k:
    if i not in l:
        c.append(i)
print(len(c))
        