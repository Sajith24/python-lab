rows=int(input("enter the number of rows:"))
step=int(input("enter the step number:"))
for i in range(1,rows+1,step):
    for j in range(1,i+1,step):
        print(i*j,end=" ")
    print("\n")    
