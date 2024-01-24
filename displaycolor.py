count=int(input("enter how much color:"))
colorlist=[]
for i in range(count):
    color=input("enter color:")
    colorlist.append(color)
print(colorlist[0]," ",colorlist[-1])
