n=int(input("Enter the limit"))
count=2
a=0
b=1
if(n==1):
    print(a)
else:
    print("Fibonacci series upto",n,"is")
    print(a)
    print(b)
    while(count<n):
        c=a+b
        print(c)
        a=b
        b=c
        count+=1
