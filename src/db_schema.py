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
    project#	Number(8),
    BusinessID	Number(9),
    projectName	Varchar2(25),
    startDate	Date,
    endDate	Date,
    projectType	Varchar2(15),
    CONSTRAINT Project_PK PRIMARY KEY(project#),
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
	project#	Number(8),
	EmpID		Number(8),
	taskName	VarChar2(20),
    description	VarChar2(100),
	CONSTRAINT Task_PK PRIMARY KEY (project#, EmpID),
	CONSTRAINT Task_FK1 FOREIGN KEY (EmpID) REFERENCES Employee(EmpID) );"""

invoice_table = """CREATE TABLE IF NOT EXISTS Invoice(
	invoice#	Number(8),
	project#	Number(8),
	invoiceDate	Date,
	totalAmt	number(8,2),
    CONSTRAINT Invoice_PK PRIMARY KEY(invoice#),
    CONSTRAINT Invoice_FK FOREIGN KEY(project#) REFERENCES Project(project#) );"""

payment_table = """CREATE TABLE IF NOT EXISTS Payment(
	payment#	Number(8),
	invoice#	Number(8),
	payDate	Date,
	Description	varchar2(100),
	Amount	number(8,2),
	payType	varchar2(15),
	bankName	varchar2(25),
	CONSTRAINT Payment_PK PRIMARY KEY(payment#),
    CONSTRAINT Payment_FK1 FOREIGN KEY (invoice#) REFERENCES Invoice(Invoice#));"""

billable_items_table = """CREATE TABLE IF NOT EXISTS Billable_Items (
    project#	Number(8),
    line#		Number(8),
    invoice#	Number(8),
    Hours		Varchar2(5),
    dateAdded	Date,
    Description	Varchar2(50),
    Cost		Number(8,2),
    Status		Varchar2(15),
    Balance	Number(8,2),
    CONSTRAINT BIllable_Items_PK PRIMARY KEY (project#,line#),
    CONSTRAINT Billable_Items_FK1 FOREIGN KEY (project#) REFERENCES Project(project#),
    CONSTRAINT Billable_Items_FK2 FOREIGN KEY (invoice#) REFERENCES Invoice(invoice#) );"""

all_tables = [business_table, project_table, employee_table, task_table, invoice_table, payment_table, billable_items_table]
