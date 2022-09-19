n=int(input())
a=-1
if n<0:
    n=a*n
    m=str(n)[::-1]
    print(a*int(m))
else:
    k=str(n)[::-1]
    print(int(k))