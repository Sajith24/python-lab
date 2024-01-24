a=int(input("range:"))
n=[]
for i in range(0,a):
    value=int(input("enter the value:"))
    if value>100:
        n.append('over')
    else:
        n.append(value)
print(n)
