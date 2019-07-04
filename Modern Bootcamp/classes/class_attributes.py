# One use of a CLASS ATTRIBUTE is to keep track of each instance of a class
class User:
    
    num_users = 0
# This is a class attribute
    
    def __init__(self, first, last, age):
        self.first = first
        self.last = last
        self.age = age
        User.num_users += 1
# First, last and age are instance attributes

    def logout(self):
        User.num_users -= 1
        return f"{self.first} has logged out!"
# Logout is an instance method. It is a method because it is applied to an object.

print(User.num_users)
user1 = User("Joe", "Smith", 56)
user2 = User("Jane", "Doe", 39)
print(User.num_users)
user2.logout()
print(User.num_users)

# Output
0  # The first print function runs but there aren't any users created yet
2 # After the two users are created num_users is incremented by 2
'Jane has logged out!' # User 2 has now run the logout function
1  # Now there is only one user left


# Another reason to use a class attribute is to limit options or validation
class Pet:
    allowed = ['Cat', 'Dog', 'Bird', 'Fish']
    def __init__(self, name, species):
        if species not in Pet.allowed:
            raise ValueError(f"You can't have {species} as a pet!")
        self.name = name
        self.species = species

# Output
cat1 = Pet("Buddy", "Fish")
print(cat1)

<__main__.Pet object at 0x00000263E9716080>

tiger = Pet("Tabby", "Tiger")

Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "<stdin>", line 5, in __init__
ValueError: You can 't have Tiger as a pet!


# Update "allowed" list
Pet.allowed.append("Whale")

# Then run...
Pet.allowed
# Output
['Cat', 'Dog', 'Bird', 'Fish', 'Whale']


# Exercise... Keep track of total eggs and num of eggs for each chicken
# My attempt
class Chicken:
    total_eggs = 0
    def __init__(self, name, species, eggs=0):
        self.name = name
        self.species = species
        self.eggs = eggs
        
    def lay_egg(self, x=0):
        Chicken.total_eggs += 1
        x = x + 1
        return x

# Exercise answer
class Chicken:
    total_eggs = 0
    def __init__(self, name, species):
        self.name = name
        self.species = species
        self.eggs = 0
    
    def lay_egg(self):
        self.eggs += 1
        Chicken.total_eggs += 1
        return self.eggs


