n = int(input())
m = n**2
s=0
while m>0:
    p=m%10
    s=s+p
    m=m//10
if n==s:
    print("Neon Number")
else:
    print("Not Neon Number")