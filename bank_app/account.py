class Account:
    balance = 0

    def __init__(self,user):
        self.user = user

    def getAccountOwner(self):
        return self.user.getName()

    def getAccountBalance(self):
        return self.balance
    
    def withdraw(self):
        amount = input('How much do you wish to withdraw?:')
        try:
            amount = int(amount)
            if self.balance < amount:
                print('Insufficient balance')
            else:
                self.balance -= amount
                print(f'Withdraw of {amount} was successful')
        except:
            print('Invalid input')    

    def deposit(self):
        amount = input('How much do you wish to deposit?:')
        try:
            amount = int(amount)
            self.balance += amount
            print(f'Deposit of {amount} made successfully')
        except:
            print('Invalid input')





