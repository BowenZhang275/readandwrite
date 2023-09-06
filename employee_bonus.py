import csv

customers = open("EmployeePay.csv", 'r')

csv_file = csv.reader(customers)

next(csv_file)

for line in csv_file:

    Firstname = line[1] 
    Lastname = line[2]

    salary = int(line[3])

    bonuspercent = line[4]
    bonus = salary * float(bonuspercent)

    totalsalary = salary + bonus

    print ("Firstname: " + Firstname)
    print ("Lastname: " + Lastname)
    print (f"Salary: $ {salary:10,.2f}")
    print (f"bonus:  $ {bonus:10,.2f}")
    print (f"Pay:    $ {totalsalary:10,.2f}")
    print ("")