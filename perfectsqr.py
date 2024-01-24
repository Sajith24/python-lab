n=int(input("Enter the limit in four digit:"))
if(n>10000):
    print("Limit exceed 4 digits")
else:
    print("Even digit perfect square between 1000 and",n)
    for i in range(1000,n,1):
        for j in range(32,100,1):
            if i==j*j:
                string=str(i)
                if(int(string[0])%2==0 and int(string[1])%2==0 and 
                  int(string[2])%2==0 and int(string[3])%2==0):
                   print(i)
