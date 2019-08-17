# Ch 7: Modules (Aug 17, 2019) 
#	via 3. Modules Python Namespaces 
#	syntax: 
#		import module_name as name_you_pick_for_the_module 
#	aka: making your own class (via object-oriented stuff and things)
#	occasionally, the wild card 	import * 
#	I doubt this will compile due module not found 
import codecademylib3_seaborn

# Add your code below:
from matplotlib import pyplot as plt

import random

numbers_a = range(1, 13)

numbers_b = random.sample(range(1000), 12)

plt.plot(numbers_a, numbers_b)

plt.show()

# more info here: 
# https://www.codecademy.com/courses/learn-python-3/lessons/modules-python/exercises/modules-python-namespaces?action=resume_content_item