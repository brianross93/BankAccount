"""Bank account Python Project for CS1.1"""


class BankAccount:

    def __init__(self, full_name, account_number, routing_number, balance):
        self.full_name = full_name
        self.account_number = account_number
        self.routing_number = routing_number
        self.balance = balance 

    #Take money out from balance amount
    def withdraw(self, amount):
        
        if self.balance < amount :
            print(f"Insufficient Funds. You have {self.balance}")
        else:
            self.balance = self.balance - amount
            print(f"Amount Withdrawn: {amount}. Your balance is {self.balance}")
    #Add money to account
    def deposit(self, amount):
        self.balance = self.balance + amount
        print(f"Your deposited {amount}. Your balance is: {self.balance}")

    #Prints current balance. Does not print account number or anything else
    def get_balance(self, balance):
        balance = self.balance
        print(f"Your balance is {balance}")
        return balance
    
    #Adds interest to balance amount
    def add_interest(self, balance):
        self.balance = round(self.balance * 1.00083, 2)
        print(f"Your balance with added interest is {self.balance}")

    #Prints Receipts
    def print_receipt(self, name, account_number, balance):
        name = self.full_name
        # This is pythonic list comprehension. It's very big brained
        account_number = [int(x) for x in str(self.account_number)] 
        
        balance = self.balance
        for i in range(4):
            account_number[i] ="*"
        #Also list comprehension
        account_number = ' '.join([str(elem) for elem in account_number])
        
        print(f"Here's your Receipt: {name}, {account_number}, ${balance}")


#Test Account Users
Howard_Starbucks = BankAccount("Howard Starbucks", 333322222, 765432, 1000) 
Howard_Starbucks.withdraw(500)
Howard_Starbucks.deposit(250)
Howard_Starbucks.get_balance(1)
Howard_Starbucks.add_interest(1)
Howard_Starbucks.print_receipt("Howard Starbucks", 333322222,1)

Suellen_Mishkin = BankAccount("Suellen Mishkin", 33335434, 87594423, 5000000)
Suellen_Mishkin.withdraw(500)
Suellen_Mishkin.deposit(250)
Suellen_Mishkin.get_balance(1)
Suellen_Mishkin.add_interest(1)
#If we only use one argument in the method, the other arguments don't matter
#Here I have Howard Starbucks as the name, but it will still print Suellen
Suellen_Mishkin.print_receipt("Howard Starbucks", 333322222,1)

Benny_Cashman = BankAccount("Benny Cashman", 77776898, 99988765, 27.54)
Benny_Cashman.withdraw(500)
Benny_Cashman.deposit(250)
Benny_Cashman.get_balance(1)
Benny_Cashman.add_interest(1)
Benny_Cashman.print_receipt("Howard Starbucks", 333322222,1)
