# program that reads the file customers.csv and 
# produces a new file containing the customer name and country they are from

import csv

customers = open("customers.csv", 'r')

csv_file = csv.reader(customers)

customer_country = open("customers_country.csv", 'w')

#skip the line
next(csv_file)

customer_country.write("Fullname, Country\n")

for record in csv_file:
    
    firstname = record[1]
    
    lastname = record[2]

    country = record[4]

    customer_country.write(f"{firstname} {lastname},{country}\n")


customer_country.close()