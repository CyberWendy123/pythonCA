# Ch 6: Strings (Aug 15)
# String Methods 

# 2. Formatting Methods 
#	.lower() - returns the string with all lowercase characters 
#	.upper() - returns the string with all uppercase characters  
#	.title() - returns the string in title case 
#		aka the first letter of each word is capitalized 
# given: 
poem_title = "spring storm"
poem_author = "William Carlos Williams"
# start code here: 
poem_title_fixed = poem_title.title()
print(poem_title_fixed)
poem_author_fixed = poem_author.upper()
print(poem_author_fixed)

# 3. Splitting Strings 
#	.split() - takes one argument 
#		and return: a list of substrings found b/t the given argument 
#		aka the delimiter 
#	syntax: 	string_name.split(delimiter)
line_one = "The sky has given over"
line_one_words = line_one.split()
print(line_one_words) # turns into a list 

# 4. Splitting Strings II 
authors = "Audre Lorde, William Carlos Williams, Gabriela Mistral, Jean Toomer, An Qi, Walt Whitman, Shel Silverstein, Carmen Boullosa, Kamala Suraiyya, Langston Hughes, Adrienne Rich, Nikki Giovanni"
# each individual author name as it's own string 
author_names = authors.split(",")
print(author_names)
# vs a list containing the last naems of the poetes in the provided string 
author_last_names = []
for name in author_names:
  	author_last_names.append(name.split()[-1])
print(author_last_names)

# 5. Splitting Strings III 
#	\n 		Newline 
#	\t 		Horizontal Tab 
spring_storm_text = \
"""The sky has given over 
its bitterness. 
Out of the dark change 
all day long 
rain falls and falls 
as if it would never end. 
Still the snow keeps 
its hold on the ground. 
But water, water 
from a thousand runnels! 
It collects swiftly, 
dappled with black 
cuts a way for itself 
through green ice in the gutters. 
Drop after drop it falls 
from the withered grass-stems 
of the overhanging embankment."""
# breaking down a list contains a string for each line of this poem 
spring_storm_lines = spring_storm_text.split('\n')

# 6. Joining Strings 
#	.join() in this syntax 
#	'delimiter'.join(list_you_want_to_join)
reapers_line_one_words = ["Black", "reapers", "with", "the", "sound", "of", "steel", "on", "stones"]
reapers_line_one = ''.join(reapers_line_one_words)

# 7. Joining Strings II 
winter_trees_lines = ['All the complicated details', 'of the attiring and', 'the disattiring are completed!', 'A liquid moon', 'moves gently among', 'the long branches.', 'Thus having prepared their buds', 'against a sure winter', 'the wise trees', 'stand sleeping in the cold.']
winter_trees_full = '\n'.join(winter_trees_lines)
print(winter_trees_full)

# 8. .strip() - removes all whitespace characters from beginning to end 
love_maybe_lines = ['Always    ', '     in the middle of our bloodiest battles  ', 'you lay down your arms', '           like flowering mines    ','\n' ,'   to conquer me home.    ']
love_maybe_lines_stripped = []
for value in love_maybe_lines:
  love_maybe_lines_stripped.append(value.strip())
love_maybe_full = '\n'.join(love_maybe_lines_stripped)
print(love_maybe_full)

# 9. Replace 
# 	with syntax: 	
#	string_name.replace(character_being_replaced, new_character)
toomer_bio = \
"""
Nathan Pinchback Tomer, who adopted the name Jean Tomer early in his literary career, was born in Washington, D.C. in 1894. Jean is the son of Nathan Tomer was a mixed-race freedman, born into slavery in 1839 in Chatham County, North Carolina. Jean Tomer is most well known for his first book Cane, which vividly portrays the life of African-Americans in southern farmlands.
"""
toomer_bio_fixed = toomer_bio.replace("Tomer", 
"Toomer")

# 10. 	.find() 
god_wills_it_line_one = "The very earth will disown you"
disown_placement = god_wills_it_line_one.find('disown')
print(disown_placement)

# 11. 	.format() 
def poem_title_card(poet, title):
  	poem_desc = "The poem \"{}\" is written by {}".format(title, poet)
 	return poem_desc

# 12. 	.format() II 
def poem_description(publishing_date, author, title, original_work): 
	poem_desc = "THe peom {title} by {author} was originally published in {original_work} in {publishing_date}.".format(publishing_date = publishing_date, author = author, title = title, original_work = original_work)
	return poem_desc
author = "Shel Silverstein"
title = "My Beard"
original_work = "Where the Sidewalk Ends"
publishing_date = "1974"
my_beard_description = poem_description(publishing_date, author, title, original_work)
print(my_beard_description)


