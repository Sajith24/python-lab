a=[]
n=int(input("enter the size of the list:"))
for i in range(1,n+1):
    print("enter the",i,"element")
    inp=input()
    a.append(inp)
max1=len(a[0])
temp=a[0]
for i in a:
    if len(i)>max1:
        max1=len(i)
        temp=i
print("the word longest length is",temp,"with",max1)
