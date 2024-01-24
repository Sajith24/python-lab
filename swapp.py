a=input("enter first word:")
b=input("enter second word:")
new_a=b[0]+a[1:]
new_b=a[0]+b[1:]
new=new_a+new_b
print("The swapped string is:",new)
