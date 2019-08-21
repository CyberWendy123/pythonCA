# CH 10 - Classes 

# 1. 	Types 
print(type(5))
my_dict = {}
print(type(my_dict))
my_list = []
print(type(my_list)) 

# 2. 	Class 
# 			= a template for a data type 
class Facade: # this is an empty class 
  pass

# 3. 	Instantiation 
facade_1 = Facade() #this variable is this class 

# 4. 	Object-Oriented Programming 
#	a class instance = an object 
facade_1_type = type(facade_1)
print(facade_1_type) # should print: <class '__main__.Facade'>

# 5. 	Class Variables 
class Grade: 
  	minimum_passing = 65
# to print this out 
harry = Grade()
print(harry.minimum_passing)

# 6. 	Methods 
class Rules:
  	def washing_brushes(self): #self = no parameters 
    	return "Point bristles towards the basin while washing your brushes."

# 7. 	Methods with Arguments 
class Circle:
  	pi = 3.14
  	def area(self, radius):
    	return Circle.pi * radius ** 2
circle = Circle()
pizza_area = circle.area(12 / 2)
teaching_table_area = circle.area(36 / 2)
round_room_area = circle.area(11460 / 2)

# 8. 	Constructors 
class Circle:
 	pi = 3.14
  	def __init__(self, diameter): 
    	print("New circle with diameter: " + str(diameter))
teaching_table = Circle(36)

# 9. 	Instance Varialbes 
#			= variables that are specific to the obb they are attached to 
class Store: 
	pass 
alternative_rocks = Store()
isabelles_ices = Store() 
alternative_rocks.store_name = "Alternative Rocks"
isabelles_ices.store_name = "Isabelle's Ices"

# 10. 	Attribute Functions 
# if neither a class variable or an instanec var of obj: pthon will throw an AttributeError 
how_many_s = [{'s': False}, "sassafrass", 18, ["a", "c", "s", "d", "s"]]
for element in how_many_s:
  	if hasattr(element, "count"):
    	print(element.count("s"))

# 11. 	Self 
class Circle:
 	 pi = 3.14
  	def __init__(self, diameter):
   		print("Creating circle with diameter {d}".format(d=diameter))
    # Add assignment for self.radius here:
    self.radius = diameter / 2
    def circumference(self):
    	return 2 * self.pi * self.radius 
medium_pizza = Circle(12)
teaching_table = Circle(36)
round_room = Circle(11460)
print(medium_pizza.circumference())
print(teaching_table.circumference())
print(round_room.circumference())

# 12. 	Everything is an Obj via using dir() function 
#	dir() is short of directory and offers an organized presentation of obj attributes 
print(dir(5))
print("\n")
def this_function_is_an_object(n): 
	return n 
print(dir(this_function_is_an_object))


# 13. 	String Representation 
class Circle:
 	pi = 3.14
  	def __init__(self, diameter):
    	self.radius = diameter / 2
  	def area(self):
    	return self.pi * self.radius ** 2
  	def circumference(self):
    	return self.pi * 2 * self.radius
  	def __repr__(self):
    	return "Circle with radius {radius}".format(radius=self.radius)
medium_pizza = Circle(12)
teaching_table = Circle(36)
round_room = Circle(11460)
print(medium_pizza)
print(teaching_table)
print(round_room)

