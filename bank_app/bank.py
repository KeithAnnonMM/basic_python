from user import User
from account import Account

class Bank:
    users = []

    def addUser(self,account):
        self.users.append(account)
    
    def userNumber(self):
        return f'There are {len(self.users)} users'

    def login(self):
        fullname = input('Enter your name:')
        for user in self.users:
            if(user.getAccountOwner() == fullname):
                print('logged in')
                while True:
                    choice = input('''
                    Select options:
                    1 - Check balance
                    2 - Deposit
                    3 - Withdraw
                    4 - Logout
                    ''')
                    if choice == '1':
                        print(f'Your account balance is :{user.getAccountBalance()}')
                    elif choice == '2':
                        user.deposit()
                    elif choice == '3':
                        user.withdraw()
                    elif choice == '4':
                        option = input('You are being logged out. Are you sure?')
                        if option.lower() == 'yes' or option.lower() == 'y':
                            self.login()
                        else:
                            pass 
                    else:
                        print('Thats not that an option')

            else:
                continue
        
user1 = User('Keith Muwanguzi','CM01094109RHTC')
account1 = Account(user1)
user2 = User('Mark Oluka','CM01094109RHTX')
account2 = Account(user2)
user3 = User('Mubeezi Michelle','CF01094119RHTC')
account3 = Account(user3)

bank = Bank()
bank.addUser(account1)
bank.addUser(account2)
bank.addUser(account3)
print(bank.userNumber())

print(bank.login())
