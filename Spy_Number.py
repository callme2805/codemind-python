n=int(input())
s=0
p=1
while n>0:
    num=n%10
    p=p*num
    s=s+num
    n=n//10
if p==s:
    print("Spy Number")
else:
    print("Not Spy Number")