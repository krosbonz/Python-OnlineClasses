class PartyAnimal:
   x = 0
   name = ''
   def __init__(self, z):
     self.name = z
     print(self.name,'constructed')

   def party(self) :
     self.x = self.x + 1
     print(self.name,'party count',self.x)

s = PartyAnimal('Sally')
j = PartyAnimal('Jim')

s.party()
j.party()
s.party()

# In object_class there was no constructor parameter except "self", but in 
# this example there is a constructor param "Sally", so name = "Sally"

# s.party() prints out "Sally" Party count 1

# j.party() replaces name = "Sally" with name = "Jim"
# def party prints out "Jim" party count 1 

# s.party() replaces name = "Jim" with name = "Sally"
# def party prints out "Sally" party count 2