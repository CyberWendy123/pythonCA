# Ch 6: Strings (Aug 15)
# Introduction of strings 

# 2. They're all Lists! 
my_name = "Wendy"
first_initial = my_name[0]
print(first_initial)

# 3. Cut Me a Slice of String 
first_name = "Rodrigo"
last_name = "Villanueva"
new_account = last_name[:5] #first five letters 
temp_password = last_name[2:6] #third through sixth letters 

# 4. Concatenating Strings 
first_name = "Julie"
last_name = "Blevins"
def account_generator(first_name, last_name): 
  	return first_name[:3] + last_name[:3] #return first three letters 
new_account = account_generator(first_name, last_name)

# 5. more string slicing 
first_name = "Reiko"
last_name = "Matsuki"
def password_generator(first_name, last_name): 
  	return str(first_name[-3:] + last_name[-3:]) #return last three letters 
temp_password = password_generator(first_name, last_name)

# 6. Negative Indices 
company_motto = "Copeland's Corporate Company helps you capably cope with the constant cacophony of daily life"
second_to_last = company_motto[-2] #second to last letter
final_word = company_motto[-4:] #last four words 

# 7. Strings are Immutable 
first_name = "Bob"
last_name = "Daily"
# first_name[0] = "R" //this is an error so instead 
fixed_first_name = "R" + first_name[-2:]

# 8. Esacpe Characters 
# some special characters like " is problematic hence.... 
password = "theycallme\"crazy\"91"

# 9. Iterating through Strings - creating our own len()! 
def get_length(word):
 	 counter = 0 
  	for x in word: # requires looping 
    	counter += 1
  	return counter 

# 10. Strings and Conditions (Part One)
def letter_check(word, letter): 
  	for x in word: 
    	if x == letter: 
      		return True
  	return False

# 11. Strings and Conditions (Part Two)
def contains(big_string, little_string): 
	return little_string in big_string 
def common_letters(string_one, string_two): 
	common = []
	for letter in string_one 
	if(letter in string_two) and not (letter in common): 
		common.append(letter)
	return common 

# 12. Review 
def username_generator(first_name, last_name):
    if len(first_name) < 3:
        user_name = first_name
    else:
        user_name = first_name[0:3]
    if len(last_name) < 4:
        user_name += last_name
    else:
        user_name += last_name[0:4]
    return user_name  
def password_generator(user_name):
    password = ""
    for i in range(0, len(user_name)):
        password += user_name[i-1]
    return password
