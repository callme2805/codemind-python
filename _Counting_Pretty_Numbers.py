t=int(input())
for i in range(1,t+1):
    count=0
    l,r=map(int,input().split())
    for i in range(l,r+1):
        if i%10==2 or i%10==3 or i%10==9:
            count+=1
    print(count)