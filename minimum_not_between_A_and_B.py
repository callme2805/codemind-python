n=int(input())
l=list(map(int,input().split()))
a,b=map(int,input().split())
k=[]
s=0
for i in l:
    if i<a or i>b:
        k.append(i)
        s=1
if s==1:
    print(min(k))
else:
    print('-1')