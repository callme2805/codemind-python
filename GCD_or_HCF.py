n,m=map(int,input().split())
l=[]
p=[]
q=[]
for i in range(1,n+1):
    if n%i==0:
        l.append(i)
for j in range(1,m+1):
    if m%j==0:
        p.append(j)
for k in l:
    if k in p:
        q.append(k)
print(q[-1])