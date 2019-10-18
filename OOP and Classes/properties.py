class Human:
    def __init__(self, first, last, age):
        self.first = first
        self.last = last
        self.age = age
    
    @property
    def full_name(self):
        return f"{self.first} {self.last}"
        
    @full_name.setter
    def full_name(self, name):
# Used to set or change 

jane = Human("Jane", "Jones", 27)

print(jane.full_name)
# When using "@property" you don't need to call it as a method "jane.full_name()" 
# with brackets
jane.full_name = 'Tim Jackson'
print(jane.full_name)
# Output
Jane Jones
Tim Jackson