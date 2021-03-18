from faker import Faker
import random
import datetime
import csv
fake = Faker()

csvTable = []

# business_table, BusinessID, busName, busAddress, busPhone, cellPhone, Revenue, foundingDate, busType
def businessTable():
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
	busAddress = busAddress.replace("\n", " ")
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
	foundingDate = fake.date_between_dates(date_start=datetime.date(1970, 1, 1), date_end= datetime.date(1990, 1, 1))
	business_table.append(foundingDate)

	# WARNING busType
	busType = fake.job()
	business_table.append(busType)
	return (BusinessID, business_table)


# project_table, projectNum, BusinessID, projectName, startDate, endDate, projectType
def projectTable(BusinessID):

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
	endDate = fake.date_between_dates(date_start = datetime.date(2016, 1, 1), date_end = datetime.date(2021, 1, 1))
	project_table.append(endDate)

	# projectType
	projectType = fake.text(max_nb_chars=15)
	project_table.append(projectType)
	
	return (projectNum, project_table)


# employee_table, EmpID, name, address, busPhone, cellPhone, empType
def employeeTable():
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
	address = address.replace("\n", " ")
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
	
	return (EmpID, employee_table)

# task_table, projectNum, EmpID, taskName, description
def taskTable(projectNum, EmpID):
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
	descriptionTask.replace('\n', ' ')
	task_table.append(descriptionTask)
	
	return task_table


# invoice_table, invoiceNum, projectNum, invoiceDate, totalAmt
def invoiceTable(projectNum):
	# invoice_table
	invoice_table = ['invoice_table']

	# invoiceNum
	invoiceNum = random.randint(10000000, 100000000)
	invoice_table.append(invoiceNum)

	# projectNum
	invoice_table.append(projectNum)

	# innvoiceDate
	invoiceDate = fake.date_between_dates(date_start = datetime.date(2015, 1, 1), date_end= datetime.date(2021, 1, 1))
	invoice_table.append(invoiceDate)

	# totalAmt
	totalAmt = 0
	invoice_table.append(totalAmt)

	# balance
	bal = totalAmt
	invoice_table.append(bal)
	
	return (invoiceNum, invoice_table)


# payment_table, invoiceNum, payDate, Description, amount, payType, bankName
def paymentTable(invoiceNum):
	# payment_table
	payment_table = ['payment_table']

	# paymentNum
	paymentNum = random.randint(10000000, 100000000)
	payment_table.append(paymentNum)

	# invoiceNum
	payment_table.append(invoiceNum)

	# payDate
	payDate = fake.date_between_dates(date_start= datetime.date(2015, 1, 1), date_end= datetime.date(2021, 1, 1))
	payment_table.append(payDate)

	# description
	descriptionInvoice = fake.text(max_nb_chars=100)
	descriptionInvoice.replace('\n', ' ')
	payment_table.append(descriptionInvoice)

	# amount
	payAmt1 = random.randint(100000, 1000000)
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
	
	return (paymentNum, payment_table)

# billable_items_table, projectNum, lineNum, invoiceNum, Hours, dateAdded, Description, Cost, Status, Balance
def billableTable(projectNum, invoiceNum):
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
	dateAdded = fake.date_between_dates(date_start= datetime.date(2015, 1, 1), date_end= datetime.date(2021, 1, 1))
	billable_items_table.append(dateAdded)

	# description
	descriptionItems = fake.text(max_nb_chars=50)
	billable_items_table.append(descriptionItems)

	# cost
	cost1 = random.randint(100000, 1000000)
	cost2 = random.randint(10, 100)
	cost2 = float(cost2)
	cost2 = cost2/100
	cost = cost1+cost2
	billable_items_table.append(cost)

	# status
	status = fake.text(max_nb_chars=15)
	billable_items_table.append(status)
	
	return (lineNum, billable_items_table)

businessIDList = []
projectNumList = []
empIDList = []
lineNumList = []
paymentNumList = []
invoiceNumList = []

# creating business tables
for i in range(0, random.randint(1, 3)):
	business = businessTable()
	csvTable.append(business[1])
	businessIDList.append(business[0])
		
# creating project tables
for busID in businessIDList:		
	for i in range(0, random.randint(1, 3)):
		project = projectTable(busID)
		csvTable.append(project[1])
		projectNumList.append(project[0])

# creating employee tables			
for i in range(0, random.randint(5, 10)):
	employee = employeeTable()
	csvTable.append(employee[1])
	empIDList.append(employee[0])

# creating task tables
for projNum in projectNumList:
	for i in range(0, random.randint(3, 10)):	
		empID = random.choice(empIDList)
		task = taskTable(empID, projNum)
		csvTable.append(task)

# creating billable item tables	
for projNum in projectNumList:
	invoice = invoiceTable(projNum)
	for i in range(0, random.randint(3, 10)):
		billable_item = billableTable(projNum, invoice[0])
		csvTable.append(billable_item[1])
		lineNumList.append(billable_item[0])
		invoice[1][-1] += billable_item[1][-2]
		invoice[1][-2] += billable_item[1][-2]
	csvTable.append(invoice[1])
	invoiceNumList.append(invoice[0])

# creating invoice tables
for i in range(0, random.randint(3, 5)):
	projectNum = random.choice(projectNumList)
	invoice = invoiceTable(projectNum)
	csvTable.append(invoice[1])
	invoiceNumList.append(invoice[0])

# creating payment tables	
for i in range(0, random.randint(3, 5)):
	invoiceNum = random.choice(invoiceNumList)
	payment = paymentTable(invoiceNum)
	csvTable.append(payment[1])
	paymentNumList.append(payment[0])	


with open("testData.csv","a+") as my_csv:
    csvWriter = csv.writer(my_csv,delimiter='|')
    csvWriter.writerows(csvTable)
