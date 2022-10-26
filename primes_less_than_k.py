n=int(input())
m=list(map(int,input().split()))
l=int(input())
k=[]
for i in m:
    cnt=0
    for j in range(1,i+1):
        if i%j==0:
            cnt+=1
    if cnt==2:
        k.append(i)
c=0
for i in k:
    if i<=l:
        c+=1
print(c)