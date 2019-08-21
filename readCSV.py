# Ch 9: Files (Aug 21) 
# 8. 	Reading a CSV file 
import csv 

with open('cool_csv.csv') as cool_csv_file: 
	cool_csv_dict = csv.DictReader(cool_csv_file)
	for row in cool_csv_dict: 
		print(row['Cool Fact'])