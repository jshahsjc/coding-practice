class User:
   def __init__(self, name, age):
      self.name = name
      self.age = age

   def century(self):
      return "User %s will turn 100 in year %d"%(self.name, (2120 - self.age))

   def adult(self):
      if self.age > 18:
         return "User %s is an adult"%self.name
      else:
         return "User %s is a minor"%self.name

User1 = User("Patrick", 5)
User2 = User("Gallilio", 55)

print User1.century()
print User2.century()
print User1.adult()
print User2.adult()
