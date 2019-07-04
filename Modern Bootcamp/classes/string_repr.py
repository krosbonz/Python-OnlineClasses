# The dundar method __repr__ is one of several ways to provide a
# nicer STRING representation of an instance

class User:
    active_users = 0

    @classmethod
    def display_active_users(cls):
        return f"There are currently {cls.active_users} active users"

    @classmethod
    def from_string(cls, data_str):
        first,last,age = data_str.split(",")
        return cls(first, last, int(age))

    def __repr__(self):
        return f"{self.first} is {self.age} years old"
    
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
print(tom)

# Output
Tom is 60 years old