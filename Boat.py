class boat:
  def __init__(self, name, type, material, speed):
    self.name = name
    self.type = type
    self.material = material
    self.speed = speed


  def __str__(self):
    return self.name + " is a " + self.type + " styled boat made out of " + self.material + " its top speed is " + self.speed + "."

  def __eq__(self, boat2):
    return self.name == boat2.name and self.type == boat2.type and self.material == boat2.material and self.speed == boat2.speed
    
  def boat_upgrade(self, material):
    boatmaterial = input("What material would you like to chage the boat to?: ")
    self.material = boatmaterial
    print("Youre boat is now made out of " + str(self.material))


  def boat_rename(self, name):
    newname = input("What would you like the new boat name to be?: ")
    self.name = newname
    print("The boat is now called " + self.name)
