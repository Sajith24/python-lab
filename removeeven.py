num=int(input("Enter the limit:"))
list=[]
for i in range(num):
    number=int(input("Enter the numbers:"))
    if number%2!=0:
        list.append(number)
print(list)
