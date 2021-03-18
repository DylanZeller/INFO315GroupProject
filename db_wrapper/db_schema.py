business_table = """CREATE TABLE IF NOT EXISTS Business (
    BusinessID	Number(9),
    busName	varchar2(25),
    busAddress	Varchar2(80),
    busPhone	Number(10),
    cellPhone	Number(10),
    Revenue	Number(8,2),	
    foundingDate 	Date,
    busType	Varchar2(20),
    CONSTRAINT Business_PK PRIMARY KEY (BusinessID) );"""

project_table = """CREATE TABLE IF NOT EXISTS Project (
    projectNum	Number(8),
    BusinessID	Number(9),
    projectName	Varchar2(25),
    startDate	Date,
    endDate	Date,
    projectType	Varchar2(15),
    CONSTRAINT Project_PK PRIMARY KEY(projectNum),
    CONSTRAINT Project_FK1 FOREIGN KEY (BusinessID) REFERENCES Business(BusinessID) );"""

employee_table = """CREATE TABLE IF NOT EXISTS Employee (
	EmpID		Number(8),
	name		VarChar2(40),
	address		VarChar2(80),
	busPhone	Number(10),
	cellPhone	Number(10),
	empType	VarChar2(25),
	CONSTRAINT Employee_PK PRIMARY KEY (EmpID) );"""

task_table = """CREATE TABLE IF NOT EXISTS Task (
	projectNum	Number(8),
	EmpID		Number(8),
	taskName	VarChar2(20),
    description	VarChar2(100),
	CONSTRAINT Task_PK PRIMARY KEY (projectNum, EmpID),
	CONSTRAINT Task_FK1 FOREIGN KEY (EmpID) REFERENCES Employee(EmpID) );"""

invoice_table = """CREATE TABLE IF NOT EXISTS Invoice(
	invoiceNum	Number(8),
	projectNum	Number(8),
	invoiceDate	Date,
	totalAmt	number(8,2),
    Balance	Number(8,2),
    CONSTRAINT Invoice_PK PRIMARY KEY(invoiceNum),
    CONSTRAINT Invoice_FK FOREIGN KEY(projectNum) REFERENCES Project(projectNum) );"""

payment_table = """CREATE TABLE IF NOT EXISTS Payment(
	paymentNum	Number(8),
	invoiceNum	Number(8),
	payDate	Date,
	Description	varchar2(100),
	Amount	number(8,2),
	payType	varchar2(15),
	bankName	varchar2(25),
	CONSTRAINT Payment_PK PRIMARY KEY(paymentNum),
    CONSTRAINT Payment_FK1 FOREIGN KEY (invoiceNum) REFERENCES Invoice(InvoiceNum));"""

billable_items_table = """CREATE TABLE IF NOT EXISTS Billable_Items (
    projectNum	Number(8),
    lineNum		Number(8),
    invoiceNum	Number(8),
    Hours		Varchar2(5),
    dateAdded	Date,
    Description	Varchar2(50),
    Cost		Number(8,2),
    Status		Varchar2(15),
    CONSTRAINT BIllable_Items_PK PRIMARY KEY (projectNum,lineNum),
    CONSTRAINT Billable_Items_FK1 FOREIGN KEY (projectNum) REFERENCES Project(projectNum),
    CONSTRAINT Billable_Items_FK2 FOREIGN KEY (invoiceNum) REFERENCES Invoice(invoiceNum) );"""

ALL_TABLES = [business_table, project_table, employee_table, task_table, invoice_table, payment_table, billable_items_table]
