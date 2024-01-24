a1=int(input("range:"))
list1=[]
for i in range(a1):
       value=int(input("elements:"))
       list1.append(value)
a2=int(input("range:"))
list2=[]
for i in range(a2):
       value=int(input("elements:"))
       list2.append(value)
if(a1==a2):
                 print("samelength")
else:
    print("not same length")
if(sum(list1)==sum(list2)):
    print("same sum")
else:
    print("not same sum")
list3=[x for x in list1 if x in list2]
print("same members are:",list3)
    
    
       
