n=input()
reverse=""
for i in n:
    reverse=i+reverse
n=int(n)
reverse=int(reverse)
s1=n**2
s2=reverse**2
s2=str(s2)
s1=str(s1)
if s2[::-1]==s1:
    print("True")
else:
    print("False")