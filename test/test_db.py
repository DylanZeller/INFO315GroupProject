import unittest
import tempfile
from db_wrapper.database import Database
from db_wrapper.db_schema import employee_table, invoice_table, payment_table, billable_items_table, balance_trigger, bi_trigger, bi_trigger_ne

class TestDatabase(unittest.TestCase):

    def setUp(self):
        self.database_file = tempfile.NamedTemporaryFile(delete=False)
        self.db = Database(self.database_file.name)

    def tearDown(self):
        self.database_file.close()

    def test_db_connects(self):
        self.assertTrue(self.db.conn is not None)

    def test_insert(self):
        self.db.create_table(employee_table)
        ins_args = ['1', 'Dylan Zeller', '123 Wallace Street, Philadelphia, PA 19104', '1234567890', '9874563210', 'Manager']
        self.db.insert('employee', ins_args)
        row = self.db.select('employee', '*')[0]
        for i in range(len(ins_args)):
            self.assertTrue(ins_args[i] == str(row[i]))

    def test_delete(self):
        self.db.create_table(employee_table)
        ins_args = ['1', 'Dylan Zeller', '123 Wallace Street, Philadelphia, PA 19104', '1234567890', '9874563210', 'Manager']
        self.db.insert('employee', ins_args)
        self.db.delete('employee', ['EmpID = 1'])
        self.assertTrue(self.db.select('employee', '*') == [])

    def test_update(self):
        self.db.create_table(employee_table)
        ins_args = ['1', 'Dylan Zeller', '123 Wallace Street, Philadelphia, PA 19104', '1234567890', '9874563210', 'Manager']
        self.db.insert('employee', ins_args)
        self.db.update('employee', ['EmpID = 2'], ['name = \'Dylan Zeller\''])
        empID = self.db.select('employee', '*')[0][0]
        print(empID)
        self.assertTrue(empID == 2)

    def test_trigger_payment(self):
        self.db.create_table(invoice_table)
        self.db.create_table(payment_table)
        self.db.execute_cmd(balance_trigger)
        invoice_ins = ['123', '1', '2021-03-19', '200', '200']
        self.db.insert('invoice', invoice_ins)
        payment_ins = ['1', '123', '2021-03-19', 'TestingTrigger', '100', 'Credit Card', 'BoA']
        self.db.insert('payment', payment_ins)
        balance = self.db.select('invoice', ['balance'], ['invoiceNum = 123'])[0][0]
        self.assertTrue(balance == 100)

    def test_trigger_update(self):
        self.db.create_table(invoice_table)
        self.db.create_table(billable_items_table)
        self.db.execute_cmd(bi_trigger)
        invoice_ins = ['123', '1', '2021-03-19', '200', '200']
        self.db.insert('invoice', invoice_ins)
        bi_ins = ['1', '1', '123', '2', '2021-03-19', 'description', '100.00', 'Done']
        self.db.insert('billable_items', bi_ins)
        amt = self.db.select('invoice', ['totalAmt'], ['invoiceNum = 123'])[0][0]
        self.assertTrue(amt == 300)

    def test_trigger_update_ne(self):
        self.db.create_table(invoice_table)
        self.db.create_table(billable_items_table)
        self.db.execute_cmd(bi_trigger_ne)
        bi_ins = ['1', '1', '123', '2', '2021-03-19', 'description', '100.00', 'Done']
        self.db.insert('billable_items', bi_ins)
        amt = self.db.select('invoice', ['totalAmt'])[0][0]
        self.assertTrue(amt == 100)



if __name__ == '__main__':
    unittest.main()