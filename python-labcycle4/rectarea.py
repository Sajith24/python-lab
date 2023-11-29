class rectangle:
    def __init__(self,length,breadth):
        self.__length=length
        self.__breadth=breadth
    def calc__area(self):
        self.__area=self.__length*self.__breadth
        print("area is:",self.__area)
        return(self.__area)
    def calc__perimeter(self):
        self.__perimeter= 2*(self.__length + self.__breadth)
        print("perimeter is:",self.__perimeter)
length1=int(input("enter length1:"))
breadth1=int(input("enter breadth1:"))
length2=int(input("enter length2:"))
breadth2=int(input("enter breadth2:"))
obj1=rectangle(length1,breadth1)
obj2=rectangle(length2,breadth2)
r1=obj1.calc__area()
r2=obj2.calc__area()
obj1.calc__perimeter()
obj2.calc__perimeter()
if r1<r2:
    print("rect 1 has larger area")
else:
    print("rect 2  has a larer area")
