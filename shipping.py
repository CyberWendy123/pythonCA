# based on Ch 3: Control Flow 
# by Wendy Xiao (Aug 11, 2019)
from __future__ import division

# cost of ground shipping 
def groundShipping(w): #where w = weight 
	if w < 2 : 
		return (1.50 * w) + 20 
	elif (w > 2) and (w <= 6): 
		return (3 * w) + 20
	elif (w > 6) and (w <= 10): 
		return (4 * w) + 20 
	else: 
		return (4.75 * w) + 20 
print(groundShipping(8.4))

# cost for drone shipping 
def droneShipping(w): 
	if w < 2: 
		return (4.5 * w)
	elif (w > 2) and (w <= 6): 
		return (9 * w)
	elif (w > 6) and (w <= 10): 
		return (12 * w)
	else: 
		return (14.25 * w)
print(droneShipping(1.5))

#premium ground shipping 
premGroundShipping = 125 

def cheaperOption(w): 
	#ground shipping is cheapest 
	ground = groundShipping(w) 
	drone = droneShipping(w)
	if(ground < drone) and (ground < premGroundShipping): 
		print("Cheapest Method is Ground Shipping costing: " + str(ground))
	elif (drone < ground) and (drone < premGroundShipping): 
		print("Cheapest Method is Drone Shipping costing: " + str(drone))
	else : 
		print("Cheapest Method is Premium Shipping costing: " + str(premGroundShipping))
cheaperOption(4.8)
cheaperOption(41.5)