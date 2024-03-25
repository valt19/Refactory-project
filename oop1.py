#defining an object in python.
#we use a keyword class followed by the name starting with a capital letter.

class Animal:
    color = ""
    size = ""
    sex = ""
    name = ""
    sound = ""
    species = ""
    age = 0
    def feed(self):# this is a method
      print("by chewing")

#a function of a class is called or refered to as a method
#creating objects of a class "Animal"
wolf = Animal()
wolf.name = "bucky"
wolf.sound = "howls"
wolf.sex = "male"
wolf.species = "grey_wolf"
wolf.size = "medium"
wolf.color = "dark_grey"
wolf.age = 7
#Accessing objects
print(f"{wolf.name} is {wolf.age}years old")
print(wolf.name + " makes " + wolf.sound)
print(f"{wolf.name} is of a {wolf.species} species")
print(f"{wolf.name} is a {wolf.sex}")
print(f"{wolf.name} is a {wolf.size} size")
print(f"{wolf.name} is {wolf.color} in color")
print(f"{wolf.feed()}")

