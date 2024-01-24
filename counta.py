fnamelist=[]
len=int(input("range:"))
for i in range(0,len):
    fname=input("enter the value:")
    fnamelist.append(fname)
count_a=0
for names in fnamelist:
    count_a+=names.count("a")
print(count_a)
