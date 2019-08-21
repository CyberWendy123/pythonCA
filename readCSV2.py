# Ch 9: Files (Aug 21) 
# 9. 	Reading Different Types of CSV Files 

import csv

with open('books.csv') as books_csv:
  books_reader = csv.DictReader(books_csv, delimiter='@')
  isbn_list = [book['ISBN'] for book in books_reader]

# based on using differet delimiters (e.g. comma or tab) 
# indicating where the values started and stopped 