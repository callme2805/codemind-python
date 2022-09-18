n=int(input())
m=list(map(int,input().split()))
p=len(m)
l=[]
for i in m:
    if i%2==0:
        l.append(i)
q=len(l)
if p==q:
    print("True")
else:
    print("False")