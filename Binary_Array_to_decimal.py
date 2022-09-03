N=int(input())
M=list(map(int,input().split()))
l=M[::-1]
s=0
for i in range(len(l)):
    s=s+int(l[i])*2**i
print(s)