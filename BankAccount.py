"""Bank account Python Project for CS1.1"""
from random import randint
routing_number = 1234567
class BankAccount:
    
    def __init__(self, full_name, account_number, balance):
        self.full_name = full_name
        self.account_number = account_number
        
        self.balance = 0

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
    def print_receipt(self):
        name = self.full_name
        balance = self.balance
        account_number = self.account_number
        # This is pythonic list comprehension. It's very big brained
        account_number = [int(x) for x in str(self.account_number)] 

        balance = self.balance
        for i in range(4):
            account_number[i] ="*"
        #Also list comprehension
        account_number = ''.join([str(elem) for elem in account_number])
    
        print(f"Here's your Receipt: {name}")
        print(f"Account Number: {account_number}, {balance}")
        print(f"Balance: {balance}")
    
    
    
def makeAccountNum():
        account_no = ""
        for i in range(8):
            account_no +=str(randint(0,9))
        return int(account_no)




#Test Account Users
Howard_Starbucks = BankAccount("Howard Starbucks", makeAccountNum(), 1000) 
Howard_Starbucks.withdraw(500)
Howard_Starbucks.deposit(250)
Howard_Starbucks.get_balance(1)
Howard_Starbucks.add_interest(1)
Howard_Starbucks.print_receipt()

Suellen_Mishkin = BankAccount("Suellen Mishkin", makeAccountNum(), 5000000)
Suellen_Mishkin.withdraw(500)
Suellen_Mishkin.deposit(250)
Suellen_Mishkin.get_balance(1)
Suellen_Mishkin.add_interest(1)
#If we only use one argument in the method, the other arguments don't matter
#Here I have Howard Starbucks as the name, but it will still print Suellen
Suellen_Mishkin.print_receipt()

Benny_Cashman = BankAccount("Benny Cashman", makeAccountNum(), 27.54)
Benny_Cashman.withdraw(500)
Benny_Cashman.deposit(250)
Benny_Cashman.get_balance(1)
Benny_Cashman.add_interest(1)
Benny_Cashman.print_receipt()

#Stretch Challenge DONE
def atmMachine():
    print("CASHMAN BANK ATM")
    action = input("Select an option: (1) Get balance, (2) Deposit (3) Withdraw")

    if action == str(1):
        print(Howard_Starbucks.print_receipt())

    elif action == str(2):
        deposit = input("Please enter your deposit amount")
        Howard_Starbucks.deposit(int(deposit))
        print(Howard_Starbucks.balance)
    elif action == str(3):
        withdraw = input("Please eneter witdraw amount")
        Howard_Starbucks.withdraw(int(withdraw))
        print(Howard_Starbucks.balance)
    else:
            print("Please select one of the following options")

atmMachine()