# Ch 8: Dictionaries (Aug 17)

# 1. what is a dictionary? 
#	- an unorder set of key: value pairs 
sensors =  {"living room": 21, "kitchen": 23, "bedroom": 20, "pantry": 22}
#num_cameras = {"backyard": 6  "garage": 2 "driveway": 1}
# 	this runs errors due to lack of commas 
print(sensors)

# 2. Make a Dictionary 
#	tip: you can also mix and match key and value types! 
translations = {"mountain":"orod", "bread":"bass", "friend":"mellon", "horse":"roch"}

# 3. Invalid Keys 
children = {"von Trapp":["Johannes", "Rosmarie", "Eleonore"] , "Corleone":["Sonny", "Fredo", "Michael"]}

# 4. Empty Dictionary 
empty_dict = {}

# 5. Add a Key 
#	via syntax: 	my_dict["new_key"] = "new_value"
animals_in_zoo = {}
animals_in_zoo["zebras"] = 8 
animals_in_zoo["monkeys"] = 12
animals_in_zoo["dinosaurs"] = 0
print(animals_in_zoo)

# 6. Add Multiple Keys 	via using .update() 
user_ids = {"teraCoder": 9018293, "proProgrammer": 119238}
user_ids.update({"theLooper":138475, "stringQueen":85739})
print(user_ids)

# 7. Overwrite values 
oscar_winners = {"Best Picture": "La La Land", "Best Actor": "Casey Affleck", "Best Actress": "Emma Stone", "Animated Feature": "Zootopia"}
oscar_winners["Supporting Actress"] = "Viola Davis"
oscar_winners["Best Picture"] = "Moonlight"

# 8. List Comprehensions of Dictionaries 
drinks = ["espresso", "chai", "decaf", "drip"]
caffeine = [64, 40, 0, 120]
zipped_drinks = zip(drinks, caffeine)
drinks_to_caffeine = {key: value for key, value in zipped_drinks}



# 9. Review 
songs = ["Like a Rolling Stone", "Satisfaction", "Imagine", "What's Going On", "Respect", "Good Vibrations"]
playcounts = [78, 29, 44, 21, 89, 5]

plays = {song:playcount for [song, playcount] in zip(songs, playcounts)}

plays["Respect"] = 94
plays["Purple Haze"] = 1

library = {"The Best Songs": plays, "Sunday Feelings": {}}

print(library)




