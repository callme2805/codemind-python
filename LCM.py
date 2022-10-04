a,b=map(int,input().split())
c=max(a,b)
d=min(a,b)
i=1
while 1:
    m=c*i
    if m%d==0:
        break
    else:
        i+=1
print(m)
