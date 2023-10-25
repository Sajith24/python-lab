num=int(input("enter the number:"))
print("factor of",num,"are\n")
for i in range(1,num+1):
    if num%i==0:
        print(i)
