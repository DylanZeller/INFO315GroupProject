from faker import Faker
import random
import datetime
import csv
fake = Faker()

csvTest = []
# business_table, BusinessID, busName, busAddress, busPhone, cellPhone, Revenue, foundingDate, busType
# business_table
business_table = ['business_table']	

# BusinessID
BusinessID = random.randint(100000000, 1000000000)
business_table.append(BusinessID)

# busName
busName = fake.company()
business_table.append(busName)

# busAddress
busAddress = fake.address()
business_table.append(busAddress)

# busPhone
busPhone = random.randint(1000000000, 10000000000)
business_table.append(busPhone)

# cellPhone
cellPhone= random.randint(1000000000, 10000000000)
business_table.append(cellPhone)

# revenue
rev1 = random.randint(100000, 1000000)
rev2 = random.randint(10, 100)
rev2 = float(rev2)
rev2 = rev2/100
Revenue = rev1+rev2
business_table.append(Revenue)

# foudningDate
foundingDate = fake.date_between_dates(date_start=datetime.date(1900, 1, 1), date_end= datetime.date(2005, 1, 1))
business_table.append(foundingDate)

# WARNING busType
busType = fake.job()
business_table.append(busType)


# project_table, projectNum, BusinessID, projectName, startDate, endDate, projectType
# project_table
project_table = ['project_table']

# projectNum
projectNum = random.randint(10000000, 100000000)
project_table.append(projectNum)

# BusinessID 
project_table.append(BusinessID)

# WARNING projectName
projectName = fake.text(max_nb_chars=15)
project_table.append(projectName)

# startDate
startDate = fake.date_between_dates(date_start=datetime.date(2006, 1, 1), date_end= datetime.date(2015, 1, 1))
project_table.append(startDate)

# endDate
endDate = fake.date_between_dates(date_start=datetime.date(2016, 1, 1), date_end= datetime.date(2021, 1, 1))
project_table.append(endDate)

# projectType
projectType = fake.text(max_nb_chars=15)
project_table.append(projectType)


# employee_table, EmpID, name, address, busPhone, cellPhone, empType
# employee_table
employee_table= ['employee_table']

# EmpID
EmpID = random.randint(10000000, 100000000)
employee_table.append(EmpID)

# name
name = fake.name()
employee_table.append(name)

# address
address = fake.address()
employee_table.append(address)

# busPhone
busPhoneEmp = random.randint(1000000000, 10000000000)
employee_table.append(busPhoneEmp)

# cellPhone
cellPhoneEmp= random.randint(1000000000, 10000000000)
employee_table.append(cellPhoneEmp)

# empType
empType= fake.job()
employee_table.append(empType)

# task_table, projectNum, EmpID, taskName, description
# task_table
task_table = ['task_table']

# projectNum
task_table.append(projectNum)

# EmpID
task_table.append(EmpID)

# taskName
taskName = fake.text(max_nb_chars=20)
task_table.append(taskName)

# description
descriptionTask = fake.text(max_nb_chars=100)
task_table.append(descriptionTask)


# invoice_table, invoiceNum, projectNum, invoiceDate, totalAmt
# invoice_table
invoice_table = ['invoice_table']

# invoiceNum
invoiceNum = random.randint(10000000, 100000000)
invoice_table.append(invoiceNum)

# projectNum
invoice_table.append(projectNum)

# innvoiceDate
invoiceDate = fake.date_between_dates(date_start=startDate, date_end=endDate)
invoice_table.append(invoiceDate)

# totalAmt
invAmt1 = random.randint(100000, rev1)
invAmt2 = random.randint(10, 100)
invAmt2 = float(invAmt2)
invAmt2 = invAmt2/100
totalAmt = invAmt1+invAmt2
invoice_table.append(totalAmt)


# payment_table, invoiceNum, payDate, Description, amount, payType, bankName
# payment_table
payment_table = ['payment_table']

# paymentNum
paymentNum = random.randint(10000000, 100000000)
payment_table.append(paymentNum)

# invoiceNum
payment_table.append(invoiceNum)

# payDate
payDate = fake.date_between_dates(date_start=invoiceDate, date_end=endDate)
payment_table.append(payDate)

# description
descriptionInvoice = fake.text(max_nb_chars=100)
payment_table.append(descriptionInvoice)

# amount
payAmt1 = random.randint(100000, invAmt1)
payAmt2 = random.randint(10, 100)
payAmt2 = float(payAmt2)
payAmt2 = payAmt2/100
payAmt = payAmt1+payAmt2
payment_table.append(payAmt)

# payType
payType = fake.text(max_nb_chars=15)
payment_table.append(payType)

# bankName
bankName= fake.company()
payment_table.append(bankName)

# billable_items_table, projectNum, lineNum, invoiceNum, Hours, dateAdded, Description, Cost, Status, Balance
# billable_items_table
billable_items_table = ['billable_items_table']

# projectNum
billable_items_table.append(projectNum)

# lineNum
lineNum = random.randint(10000000, 100000000)
billable_items_table.append(lineNum)

# hours
hours = random.randint(1,10000)
billable_items_table.append(hours)

# dateAdded
dateAdded = fake.date_between_dates(date_start=invoiceDate, date_end=endDate)
billable_items_table.append(dateAdded)

# description
descriptionItems = fake.text(max_nb_chars=50)
billable_items_table.append(descriptionItems)

# cost
cost1 = random.randint(100000, rev1)
cost2 = random.randint(10, 100)
cost2 = float(cost2)
cost2 = cost2/100
cost = cost1+cost2
billable_items_table.append(cost)

# status
status = fake.text(max_nb_chars=15)
billable_items_table.append(status)

# balance
bal1 = random.randint(100000, rev1)
bal2 = random.randint(10, 100)
bal2 = float(bal2)
bal2 = bal2/100
bal = bal1+bal2
billable_items_table.append(bal)

csvTest.append(business_table)
csvTest.append(project_table)
csvTest.append(employee_table)
csvTest.append(task_table)
csvTest.append(invoice_table)
csvTest.append(payment_table)
csvTest.append(billable_items_table)
with open("testData.csv","w+") as my_csv:
    csvWriter = csv.writer(my_csv,delimiter=',')
    csvWriter.writerows(csvTest)
