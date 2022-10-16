n=int(input())
s=[]
p=[]
k=[]
for i in str(n):
    if int(i)%2==0:
        s.append(i)
    elif int(i)%2:
        p.append(i)
    else:
        k.append(i)
if len(str(n))==len(s):
    print("Even")
elif len(str(n))==len(p):
    print("Odd")
else:
    print("Mixed")