class Fishy:
  def __init__(self, name, type, strength):
    self.name = name
    self.type = type
    self.strength = strength
 
  
  def __str__(self):
    return self.name + " is a " + self.type + " type fish, and has a strenght level of " + str(self.strength)

  def __eq__(self, Fish2):
    return self.name == Fish2.name and self.type == Fish2.type and self.strength == Fish2.strength

  def evolve(self, type):
    newtype = input("What type of fish is this fish evolving into?: ")
    self.type = newtype
    print("The fish is now a " + str(self.type))

  def hit_gym(self, strength):
    grindtime = int(input("How long was the fish at the gym?: "))
    grindtime = grindtime + int(self.strength)
    self.strength = grindtime
    print("The fish's new strenght is " + str(self.strength))
    
