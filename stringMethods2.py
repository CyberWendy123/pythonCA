# Ch 6: Strings (Aug 17)
# String Methods II 
# basically writing funcitons using strings 

# plus even more! 

# 2. Count Letters 
# 		writing a function taking a string parameter 
# 		and return totalnumber of unique letters in the string 
letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
def uniqueEnglishLetters(word): # goal: create this function 
	totalNum = 0 
	for l in letters: 
		if l in word: 
			totalNum += 1 
	return totalNum
print(uniqueEnglishLetters("mississippi"))
print(uniqueEnglishLetters("Apple")) 
# both should print out 4 

# 3. Count X 
