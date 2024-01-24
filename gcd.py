num1=int(input("enter the first number:"))
num2=int(input("enter the second number:"))
gcd=1
minimum=min(num1,num2)
for i in range(1,minimum):
               if num1%i==0 and num2%i==0:
                gcd=i
print("gcd of",num1,"and",num2,"is:",gcd)
               
