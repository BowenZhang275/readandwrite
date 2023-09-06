# example 
# Customer ID,Total
# 250,5255.24
# 251,26634.88
# 252,625.53
# 253,28735.62
# 254,43095.65
# 255,38747.02
# 256,95202.77
# 257,19802.72
# 258,14795.87
# 259,32874.75
# 260,29710.26
# 261,18098.01

import csv

sales = open("sales.csv", 'r')

csv_file = csv.reader(sales)

next(csv_file)

report = open("salesreport.csv", 'w')

report.write("Customer Id, Total \n")

total = 0

firstline = next(csv_file)
customer_id = firstline[0]

subtotal = float(firstline[3])
taxamt = float(firstline[4])
freight = float(firstline[5])

total = subtotal + taxamt + freight 

for line in csv_file:

    if customer_id == line[0]:

        subtotal = float(line[3])
        taxamt = float(line[4])
        freight = float(line[5])

        total = subtotal + taxamt + freight + total

    else:
        
        report.write(f"{customer_id}, {total:.2f} \n")

        total = 0
        customer_id = line[0]
        subtotal = float(line[3])
        taxamt = float(line[4])
        freight = float(line[5])

        total = subtotal + taxamt + freight

report.write(f"{customer_id}, {total:.2f} \n")

report.close()


