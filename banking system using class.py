class Bank :
    def __init__(self,accno,name,balance):
        self.accno = accno
        self.name = name
        self.balance = balance

    def show_account_info(self):
        print('\nAccount no is : ',self.accno)
        print('Customer Name is : ',self.name)
        print('balance is  : ',self.balance)


    def withdraw(self):
        w_amt=int(input("\n Enter the amount uou want to withdraw"))
        if w_amt < self.balance:
            self.balance = self.balance-w_amt
            print(f" rs.{w_amt}is succesfully withdraw")
            print(f"remaining balance is {self.balance}")
        else:
            print("insufficient balance")

    def deposit(self):
        d_amt= int (input("Enter the amount uou want to deposit"))
        balance = self.balance + d_amt
        print(f"Rs.{d_amt}is deposited to your account")
        print(f"your current balance is Rs.{balance}")

    def transfer(self):
        pass


Ac1 = Bank(101,'Rakesh',5000)
Ac2 = Bank(102,'Lalit',15000)
Ac3 = Bank(103,'Tarun',500)

Ac1.show_account_info()
Ac2.show_account_info()
Ac3.show_account_info()

Ac1.deposit()
