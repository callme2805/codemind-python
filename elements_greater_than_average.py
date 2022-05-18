n=int(input())
l=list(map(int,input().split()))
count=0
s=0
for i in l:
    s=s+i
    avg=s//n
for j in l:
    if j>=avg:
        count+=1
print(count)