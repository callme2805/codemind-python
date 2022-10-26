n,m=map(int,input().split())
a=list(map(int,input().split()))
b=list(map(int,input().split()))
k=[]
for i in a:
    if i in b:
        k.append(i)
for i in b:
    if i in a:
        k.append(i)
l=list(set(k))
print(len(l))