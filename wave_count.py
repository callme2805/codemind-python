n=int(input())
m=list(map(int,input().split()))
l=0
for i in range(1,n-1,2):
    if m[i]>m[i-1] and m[i]>m[i+1]:
        l+=1
        k=0
    else:
        k=1
        break

if k==0:
    print(l)
else:
    print('-1')

        