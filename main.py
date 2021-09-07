from Fish import Fishy
from Fisherman import Fishman
from Boat import boat


#Identification for Fish
name = "Bobby"
breed = "Zebra"
strength = "4"

#2 Fish instances to compare
Fish1 = Fishy(name, breed, strength)
Fish2 = Fishy(name, breed, strength)

#Calling Fish Functions
print(Fish1)
print(Fish1 == Fish2)
Fish1.evolve(breed)
Fish1.hit_gym(Fish1.strength)
print(Fish1)

print("")

#Identification for Fisherman
name = "Luffy"
trouser_color = "Red"
Experience = "40"

#2 Fisherman instances to compare
Fisherman1 = Fishman(name, Experience, trouser_color)
Fisherman2 = Fishman(name, Experience, trouser_color)


#Calling Fish Functions
print(Fisherman1)
print(Fisherman1 == Fisherman2)
Fisherman1.change_trousers(Fisherman1.trouser_color)
Fisherman1.fishing_time(Fisherman1.experience)
print(str(Fisherman1))

print("")

#identification for boat
Boatname = "The Sunny"
Style = "Yacht"
Material = "Steel"
Speed = "400mph" 

#Creating 2 boats
boat1 = boat(Boatname, Style, Material, Speed)
boat2 = boat(Boatname, Style, Material, Speed)

#Calling functions
print(boat1)
print(boat1 == boat2)
boat1.boat_rename(boat1.name)
boat1.boat_upgrade(boat1.material)
print(boat1)
