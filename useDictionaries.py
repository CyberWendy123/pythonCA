# Ch 8: Dictionaries (Aug 17) 
#	via using dictionaries 

# 2. Get A Key 
zodiac_elements = {"water": ["Cancer", "Scorpio", "Pisces"], "fire": ["Aries", "Leo", "Sagittarius"], "earth": ["Taurus", "Virgo", "Capricorn"], "air":["Gemini", "Libra", "Aquarius"]}
print(zodiac_elements['earth'])
print(zodiac_elements['fire'])

# 3. Get an Invalid Key 
zodiac_elements["energy"] = "Not a Zodiac element"
print(zodiac_elements["energy"])

# 4. Try/Except to Get a Key 
caffeine_level = {"espresso": 64, "chai": 40, "decaf": 0, "drip": 120}
caffeine_level['matcha'] = 30
try:
  	print(caffeine_level['matcha'])
except KeyError:
 	 print("Unknown Caffeine Level")

# 5. Safely Get a Key 
user_ids = {"teraCoder": 100019, "pythonGuy": 182921, "samTheJavaMaam": 123112, "lyleLoop": 102931, "keysmithKeith": 129384}
tc_id = user_ids.get("teraCoder", 100000)
stack_id = user_ids.get("superStackSmash", 100000)
# 100000 as the default if key does not exist 
print(tc_id)
print(stack_id)

# 6. Delete a Key 
#		by using .pop() 
available_items = {"health potion": 10, "cake of the cure": 5, "green elixir": 20, "strength sandwich": 25, "stamina grains": 15, "power stew": 30}
health_points = 20
# start coding here: 
health_points += available_items.pop("stamina grains", 0)
health_points += available_items.pop("power stew", 0)
health_points += available_items.pop("mystic bread", 0)
print(available_items)
print(health_points)

# 7. Get All Keys 
user_ids = {"teraCoder": 100019, "pythonGuy": 182921, "samTheJavaMaam": 123112, "lyleLoop": 102931, "keysmithKeith": 129384}
num_exercises = {"functions": 10, "syntax": 13, "control flow": 15, "loops": 22, "lists": 19, "classes": 18, "dictionaries": 18}
# start coding here: 
users = user_ids.keys()
lessons = num_exercises.keys()
print(users)
print(lessons)

# 8. Get All Values: 



















