q=int(input())
for i in range(1,q+1):
    num=int(input())
    i=0
    s=0
    while num!=0:
        n=num%10
        s=s+n*pow(2,i)
        num=num//10
        i+=1
    print(s)