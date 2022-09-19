n=int(input())
l=[]
for i in range(1,100):
    m=i*(i+1)
    l.append(m)
if n in l:
    print("YES")
else:
    print("NO")