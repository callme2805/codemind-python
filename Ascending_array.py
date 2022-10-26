n=int(input())
m=list(map(int,input().split()))
k=0
for i in range(0,n-1):
    if m[i]<m[i+1]:
        k+=0
    else:
        k+=1
if k==0:
    print("yes")
else:
    print("no")
        
    