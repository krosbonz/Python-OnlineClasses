# The code below works, but the idea of inheriting is to avoid duplication. 
class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species

    def __repr__(self):
        return f"{self.name} is a {self.species}"

    def make_sound(self, sound):
        print(f"This animal says {self.sound}")

class Cat(Animal):
    def __init__(self, name, species, breed, toy):
# "name" and "species" are already covered in Animal, so we shouldn't have to do this
        self.name = name
        self.species = species
        self.breed = breed
        self.toy = toy


fuzzy = Cat("Baxter", "Cat", "Scotch Fold", "String")
print(fuzzy)
# Output
Baxter is a Cat

# Here is a better way
class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species

    def __repr__(self):
        return f"{self.name} is a {self.species}"

    def make_sound(self, sound):
        print(f"This animal says {self.sound}")

class Cat(Animal):
    def __init__(self, name, breed, toy):
# In the "cat" class the species will always be cat, so we can make this change
# We will no longer have to pass in "Cat" when creating an instance of cat
        super().__init__(name, species='Cat')
# "super()" refers to the parent class. In this case "Animal"
        self.breed = breed
        self.toy = toy

fuzzy = Cat("Baxter", "Scotch Fold", "String")
print(fuzzy)
# Output
Baxter is a Cat

