n=int(input())
a=1
for i in range(2,n):
    if n%i==0:
        b=0
        for j in range(1,i+1):
            if i%j==0:
                b+=1
        if b==2:
            a=a*i
            print(i,end=" ")
if a!=n:
    print(-1)
            