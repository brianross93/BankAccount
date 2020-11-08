"""Bank account Python Project for CS1.1"""


class BankAccount:

    def __init__(self, full_name, account_number, routing_number, balance):
        self.full_name = full_name
        self.account_number = account_number
        self.routing_number = routing_number
        self.balance = balance 


    def withdraw(self, amount):
        
        if self.balance < amount :
            print(f"Insufficient Funds. You have {self.balance}")
        else:
            self.balance = self.balance - amount
            print(f"Amount Withdrawn: {amount}. Your balance is {self.balance}")
    
    def deposit(self, amount):
        self.balance = self.balance + amount
        print(f"Your deposited {amount}. Your balance is: {self.balance}")

    def get_balance(self, balance):
        balance = self.balance
        print(f"Your balance is {balance}")
        return balance
    
    def add_interest(self, balance):
        self.balance = round(self.balance * 1.00083, 2)
        print(f"Your balance with added interest is {self.balance}")

    def print_receipt(self, name, account_number, balance):
        name = self.full_name

        account_number = [int(x) for x in str(self.account_number)] 
        
        balance = self.balance
        for i in range(4):
            account_number[i] ="*"
        account_number = ' '.join([str(elem) for elem in account_number])
        
        print(f"Here's your Receipt: {name}, {account_number}, {balance}")


    # interest = balance *  0.00083

Howard_Starbucks = BankAccount("Howard Starbucks", 333322222, 765432, 1000) 
Howard_Starbucks.withdraw(500)
Howard_Starbucks.deposit(250)
Howard_Starbucks.get_balance(1)
Howard_Starbucks.add_interest(1)
Howard_Starbucks.print_receipt("Howard Starbucks", 333322222,1)