n=int(input())
l=list(map(int,input().split()))
k=l[:n//2]
m=l[n//2:]
print(abs(sum(k)-sum(m)))