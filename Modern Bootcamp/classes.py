# Classes generally have camel naming
class User():
    pass

user1 = User()
print(user1)

# Output
< __main__.User object at 0x0000020DF33C4978 >
# Creates a user object



# Classes have a __init__ method that gets called each time you create 
# an instance of a class (instantiate)
class User:
    def __init__(self, first, last, age):
# Self refers to the current instance of the class
# NOT the class itself but each instance of when the class is instantiated
# Self must be the first parameter to __init__ and any methods and properties
# on class instances
        self.first = first
        self.last = last
        self.age = age
# Creating an object that is an instance of a class is instantiating a class
user1 = User("Joe", "Smith", 56)
user2 = User("Jane", "Doe", 39)
print(user1.first, user1.last, user1.age)
print(user2.first, user2.last, user2.age)
# Output
Joe Smith 56
Jane Doe 39

# To add on...
class User:
    def __init__(self, first, last, age):
        self.first = first
        self.last = last
        self.age = age
    
    def full_name(self):
        return f"{self.first} {self.last}"
        
    def initials(self):
        return f"{self.first[0]}.{self.last[0]}."
        
    def likes(self, things):
        return f"{self.first} likes {things}"

    def is_senior(self):
        return self.age >= 65
    
    def birthday(self):
        self.age += 1
        return f"Happy {self.age}th birthday, {self.first}!"

user1 = User("Joe", "Smith", 56)

print(user1.full_name())
print(user1.initials())
print(user1.likes("cake"))
print(user1.is_senior())
print(user1.birthday())

# Output
Joe Smith
J.S.
Joe likes cake
False
Happy 57th birthday, Joe!


# Exercise...

class BankAccount:
    def __init__(self,owner, balance=0):
        self.owner = owner
        self.balance = balance
        
    def deposit(self,x):
        self.balance = x + self.balance
        return self.balance
        
    def withdraw(self,z):
        self.balance = self.balance - z
        return self.balance
        
acct = BankAccount("Darcy", 0)

# Output from these different input
acct.owner  # Darcy
acct.balance # 0
acct.deposit(10)  # 10
acct.withdraw(3)  # 7
acct.balance # 7
