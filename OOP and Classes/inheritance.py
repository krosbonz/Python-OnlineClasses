
class Animal:
    cool = True

    def make_sound(self, sound):
        print(f"This animal says {sound}")

class Cat(Animal):
    pass


# So far we have learned;
a = Animal()
a.make_sound("growl")
# Output
This animal says growl

# Now we see a class inheriting from another class
# In this case the "Cat" class is inheriting from the "Animal" class
b = Cat()
b.make_sound("meow")
# Output
This animal says meow

# In the "Animal" class "cool" is a class attribute for "Animal" but the "Cat" class
# has access to it.
print(b.cool)
print(Cat.blue)
print(Animal.cool)
# Output
True
True
True
