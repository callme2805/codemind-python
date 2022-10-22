n=int(input())
l=list(map(int,input().split()))
k=int(input())
m=[]
for i in range(n):
    if i<k:
        m.append(l[i])
print(sum(m))