# Class Methods  - Methods that are not concerned with the instances, but the class itself

# @classmethod  - Signifies the next method is a class method not an instance method

class User:
    active_users = 0

    @classmethod
    def display_active_users(cls):
        return f"There are currently {cls.active_users} active users"
# "self" isn't necessary as the class is passed in each time the method is called
# "cls" is the class object not an instance of the class
    
    def __init__(self, first, last, age):
        self.first = first
        self.last = last
        self.age = age
        User.active_users += 1

    def full_name(self):
        return f"{self.first} {self.last}"

    def logout(self):
        User.active_users -= 1
        return f"{self.first} has logged out!"


user1 = User("Joe", "Smith", 56)
user2 = User("Pete", "Jones", 45)
print(User.display_active_users())
user3 = User("Jane", "Smith", 60)
user4 = User("Patricia", "Jones", 40)
print(User.display_active_users())

# Output
There are currently 2 active users
There are currently 4 active users


# Class Methods II

class User:
    active_users = 0

    @classmethod
    def display_active_users(cls):
        return f"There are currently {cls.active_users} active users"

    @classmethod
    def from_string(cls, data_str):
        first,last,age = data_str.split(",")
        return cls(first, last, int(age))
    
    def __init__(self, first, last, age):
        self.first = first
        self.last = last
        self.age = age
        User.active_users += 1

    def full_name(self):
        return f"{self.first} {self.last}"

    def logout(self):
        User.active_users -= 1
        return f"{self.first} has logged out!"

tom = User.from_string("Tom,Harris,60")
# "tom" is the same as the previous "user1", "user2", etc...
print(tom.first)
print(tom.full_name())

# Output
Tom
Tom Harris