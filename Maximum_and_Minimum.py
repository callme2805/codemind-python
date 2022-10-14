n=int(input())
l=list(map(int,input().split()))
c=0
a=[]
for i in range(n):
    if l[i]==l.count(l[i]):
        a.append(l[i])
        c=1
if c==1:
    print(min(a),end=" ")
    print(max(a))
else:
    print("-1")