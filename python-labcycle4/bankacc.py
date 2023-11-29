class bank:
    def __init__(self,accno,name,accty,bal):
        self.accno=accno
        self.name=name
        self.accty=accty
        self.bal=0
    def showamt(self):
        print("account holder name:",self.name)
        print("account number:",self.accno)
        print("account type:",self.accty)
        print("balance:",self.bal)
    def depo(self,d1):
        self.bal=self.bal+d1
        return self.bal
    def withd(self,w1):
        self.bal=self.bal-w1
        return self.bal
n=input("enter your name:")
a=int(input("enter your acoount number:"))
t=input("enter your account type:")
o=bank(a,n,t,bal=0)
o.showamt()
while(True):
    print("\n menu")
    print("\n1.Deposit")
    print("\n2.withdraw")
    c=int(input("enter your choice:"))
    if(c==1):
        d=int(input("enter the ambount to deposit:"))
        print("you total balance is:",o.depo(d))
    elif(c==2):
        w=int(input("enter the amount to be withdrawn:"))
        if(w>d):
            print("INSUFFICIENT BALANCE")
        else:
            print("your total balance amount is",o.withd(w))
    else:
        print("enter a valid choice.")
