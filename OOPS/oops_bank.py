class Bank:
    acc_no:int
    name:str
    acc_type:str
    ifsc_code:int
    balance:int

    # instance variables-self
    #constructer >> initialize instance variable 

    def create_acc(self,acc_no,name,acc_type,ifsc_code,balance):
    #   initialize instance variale
      self.acc_no=acc_no
      self.name=name
      self.acc_type=acc_type
      self.ifsc_code=ifsc_code
      self.balance=balance

    def deposit(self,amount):
       self.balance+=amount
       print(f"your {self.acc_no} has been credited with {amount} available balance {self.balance}")

    def withdraw(self,amount):
        if amount>self.balance:
          print("Insufficent balance")
        else:
          self.balance-=amount
          print(f"Your {self.acc_no} has been debited with {amount} available balance {self.balance}")

    def get_balance(self):
       print(f"Your Available balance:{self.balance}")
       

bank1=Bank()
bank1.create_acc(123456789,"Ram","savings",11111111111,50000)

dep=int(input("Enter amount to be deposited:"))
bank1.deposit(dep)
bank1.get_balance()
with_draw=int(input("Enter amount to be withraw:"))
bank1.withdraw(with_draw)
bank1.get_balance()
        
    