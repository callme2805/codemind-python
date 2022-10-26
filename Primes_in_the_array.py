n=int(input())
l=list(map(int,input().split()))
k=[]
for i in range(n):
    cnt=0
    for j in range(1,l[i]+1):
        if l[i]%j==0:
            cnt+=1
    if cnt==2:
        k.append(l[i])
print(len(k))