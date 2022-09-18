n=int(input())
m=list(map(int,input().split()))
l=[]
for i in m:
    if i not in l:
        l.append(i)
print(*l)
    