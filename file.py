# Ch 9: Files (Aug 21)

# 1. 	Reading a File 
with open('welcome.txt') as text_file: 
  text_data = text_file.read() 
print(text_data)

# 2. 	Iterating through lines 
with open('how_many_lines.txt') as lines_doc:
  for line in lines_doc.readlines(): 
    print(line)

# 3. 	Reading a Line 
with open('just_the_first.txt') as first_line_doc:
  first_line = first_line_doc.readline()
  print(first_line)

# 4. 	Writing a File 
with open('bad_bands.txt', 'w') as bad_bands_doc: #don't forget the w! (w = write)
  bad_bands_doc.write('The Beatles')

# 5. 	Appending to a File 
with open('cool_dogs.txt', 'a') as cool_dogs_file:
  cool_dogs_file.write('Air Buddy')

# 6. 	What's with "with" ? 
# "with" keyword invokes someting called a context manager for the file we're calling 
# "open()" on - takes care of opening and closing after we leave the indented block 

# 7. 	What is a CSV File? 
# it stands for comma-separted values similar to spreadsht software(e.g. microsoft excel)
# more here: https://www.codecademy.com/courses/learn-python-3/lessons/learn-python-files/exercises/what-is-a-csv?action=resume_content_item 
with open('logger.csv') as log_csv_file: 
	print(log_csv_file.read())

# 8. 	Reading a CSV file 
# see readCSV.py 

# 9. 	Reading Different Types of CSV Files 
# see readCSV2.py

# 10. 	Writing a CSV File 
# see writeCSV.py 

# 11. Reading a JSON file 
# see readJSON.py

# 12. Write a JSON file 
# see writeJSON.py 

