n=int(input())
k=n**2
l=len(str(n))
m=k%10**l
if m==n:
    print("Automorphic Number")
else:
    print("Not an Automorphic Number")