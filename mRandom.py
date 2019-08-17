# Ch 7: Modules (Aug 17, 2019) 
#	via 2. Modules Python Random 
import random #import the random library 

# Create random_list below:
rList = [random.randint(1, 101) for i in range(101)]

# Create randomer_number below:
r = random.choice(rList)

# Print 
print(r)