class User:
    def __init__(self,first,last,password):
        self.first = first
        self.last = last
        self.password = password
        self.email = first.lower()+last.lower()+'@gmail.com'

    def checkPasswordLength(self):
        if len(self.password) < 8:
            return 'Invalid Password'
        else:
            return self.password   

    def fullname(self):
        return ('{} {}').format(self.first,self.last) 
        



fname = input('Enter your first name:')
lname = input('Enter your last name:')
password = input('Enter your password:')

user1 = User(fname,lname,password)
print(user1.checkPasswordLength())
print(user1.fullname())

