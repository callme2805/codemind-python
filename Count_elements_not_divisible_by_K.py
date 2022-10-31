n,k=map(int,input().split())
l=list(map(int,input().split()))
m=[]
for i in l:
    if i%k!=0:
        m.append(i)
print(len(m))