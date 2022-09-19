n=input()
i=1
s=0
for j in n:
    s+=int(j)**i
    i+=1
if s==int(n):
    print("True")
else:
    print("False")