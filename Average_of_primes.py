n=int(input())
m=list(map(int,input().split()))
k=[]
for i in m:
    cnt=0
    for j in range(1,i+1):
        if i%j==0:
            cnt+=1
    if cnt==2:
        k.append(i)
avg=sum(k)/len(k)
print('{:.2f}'.format(avg))