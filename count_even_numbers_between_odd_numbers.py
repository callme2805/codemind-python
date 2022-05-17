n=int(input())
l=list(map(int,input().split()))
count=0
for i in range(len(l)-2):
    if l[i]%2!=0 and l[i+2]%2!=0:
        if l[i+1]%2==0:
            count+=1
print(count)