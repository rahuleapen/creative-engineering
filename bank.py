class Account:

       def __init__(self):
          self.accno=int(input("enter the account"))
          self.name=input("enter the accountant")
          self.balance=float(input("enter the balance"))

       def withdraw(self):
            n=float(input("enter the amount")
            self.balance=self.balance-n

        def deposit(self):
            m=float(input("enter the amount"))
            self.balance=self.balance+m

        def showbalance(self):
             print(self.accno,self.name,self.balance)

x=Account()
y=Account()
z = int(input("select your account: 1.x 2.7"))
if(z==1):

    c = int(input("enter the option : 1. withdraw 2.deposit 3.show balance")
    if (c==1):
      x.withdraw()

    elif (c= 2):
      x.deposit() 
    elif (c=3) :
  x.showbalance()
    else:
  print("invalid option")

elif(z==2):

    c =int(input("enter the option : 1. withdraw 2. deposit 3.Showbalance")
    if(c==1):

      y.withdraw()

    elif(c==2):

      y.d
    elif(c==3):

      y.showbalance()
    else:

      print("invalid option")
 else:

    print("invalid account")
