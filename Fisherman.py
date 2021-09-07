class Fishman:
  def __init__(self, name, experience, trouser_color):
    self.name = name
    self.experience = experience
    self.trouser_color = trouser_color
  
  def __str__(self):
    return self.name + " is a fisherman with " + str(self.experience) + " points of experience. They are wearing " + self.trouser_color + " colored trousers"
  
  def __eq__(self, Fisherman2):
    return self.name == Fisherman2.name and self.experience == Fisherman2.experience and self.trouser_color == Fisherman2.trouser_color


  def change_trousers(self, trouser_color):
    new_trousers = input("What color should your fishermans trousers be now?: ")
    self.trouser_color = new_trousers
    print("The fisherman is now wearing " + self.trouser_color + " colored trousers")

  def fishing_time(self, experience):
    xp_gain = int(input("How long did the fisherman fish today?: "))
    xp_gain = xp_gain + int(self.experience)
    self.experience = xp_gain
    print("The fishermans experience is now " + str(self.experience))
