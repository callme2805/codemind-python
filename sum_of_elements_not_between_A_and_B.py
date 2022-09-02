N=int(input())
M=list(map(int,input().split()))
A,B=map(int,input().split())
c=[]
for i in M:
    if i<A or i>B:
        c.append(i)
print(sum(c))